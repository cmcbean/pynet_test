#!/usr/bin/env python

from getpass import getpass
from netmiko import ConnectHandler

def main():
   sw1_pass = getpass("Enter switch password: ")
 
   pynet_sw1 = {
       'device_type': 'arista_eos',
       'ip': '184.105.247.72',
       'username': 'pyclass',
       'password': sw1_pass,
}

   cfg_commands = {
       'vlan 701',
       'name orange',
}

   net_connect = ConnectHandler(**pynet_sw1)
   print "Current Prompt: " + net_connect.find_prompt()

   print "\nConfiguring VLAN"
   print "#" * 80
   print
   output = net_connect.send_config_set(cfg_commands)
   print output
   print "#" * 80 

   print "\nConfiguring VLAN from file"
   print "#" * 80
   print
   output = net_connect.send_config_from_file("vlan_cfg.txt")
   print output
   print "#" * 80
   print


if __name__ == "__main__":
   main()
