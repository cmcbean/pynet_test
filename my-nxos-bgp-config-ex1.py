#!/usr/bin/env python

from pprint import pprint
import time
from getpass import getpass

import request
from request.packages.urllib3.exceptions import InsecureRequestWarning

from pynxos.device import Device
from pynxos.errors import CLIError

# Disable untrusted CERT warnings
request.packages.urllib3.disable_warnings(InsecureRequestWarning)

def config_patterna(nxs_obj, pattern):
  """search running-configu for pattern.  Display to stdout."""
  print
  print nxs_obj.show("show hostname")
  print '_' * 30
  config =  nxs_obj.show("show run", raw_text=True)
  for line in config.splitlines():
    if pattern in line:
      print line

def check_nxapi_errors(results, verbose=False):
  """Return Trune if all commands are None"""
  for entry in results:
    if entry is not None:
      if verbose:
        print entry
      return False
  return True

def main():
  """Configure BGP usig NX-API."""
  # Nexux Switches
  switch_ip = rew_input("enter Switch IP: ")
  username = 'pyclass'
  password = getpass()
  eth_intf = "Ethernet 2/1"
  intf_ip = '10.31.2.11/24'
  peer_ip = '10.31.2.1'
  as_number = '10'

  config_eth = [
      'interface ' + eth_intf,
      'ip address ' + intf_ip
  ]


  config_bgp = [
      'feature bgp',
      'router bgp ', + as_number,
      'neighbor {} remote-as {}'.format(peer_ip, as_number),
      'address-family ipv4 unicast',
  ]

  nxs = Device(host=switch_ip, username=username, password=password, transport='https', port=8443)
  
  print "\nCurrent Ethernet Config: "
  cmd = 'show run int {}'.format(eth_intf)
  print nxs.show(cmd, raw_text=True)

  print "\nConfig Ethernet Interface:"
  results = nxs.config_list(config_eth)
  if check_nxapi_results(results):
    print "...Interface Configured Sucessfully."
  
  print "\nCurrent Ethernet Config: "
  cmd = 'show run int {}'.format(eth_intf)
  print nxs.show(cmd, raw_text=True)

  print
  print "-" * 50
  print "BGP Config"
  print "-" * 50
 

  cmd = 'show run bgp'
  print nxs.show(cmd, raw_text=True)

  print "\nConfigure BGP"
  results = nxs.config_list(config_bgp)
  if check_nxapi_errors(results):
    print "...BGP configured sucessfully."

  cmd = 'show run bgp'
  print nxs.show(cmd, raw_text=True)


  print "\nVerify BGP (requires both peers)."
  print "Sleeping..."
  time.sleer(15)
  cmd = 'show bgp session'
  bgp_out = nxs.show(cmd)
  pprint(bgp_out)

  print "\Saving config.."
  print nxs.save()

if __name__ == "__main__":
    main()

