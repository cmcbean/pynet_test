#!/usr/bin/env python

"""

Execute 'show interfaces' on the Arista Switch using eapi.

Extract the interfaceCounters inOctets/outOctetc for all the interfaces
that have this information.


"""

import pyeapi


def main():
  """

  Execute 'show interfaces' on the Arista Switch using eapi.

  Extract the interfaceCounters inOctets/outOctetc for all the interfaces
  that have this information.

  """

  pynet_sw = pyeapi.connect_to("pynet-sw1")
  show_int = pynet_sw.enable("show interfaces")
  show_int = show_int[0]['result']['interfaces']
  print "\n{:>15} {:>15} {:>15}".format("Interface", "inOctets", "outOctets")
  sep = "-" * 15
  print "\n{:>15} {:>15} {:>15}".format(sep, sep, sep)
  for intf, v in show_int.items():
    intf_counters = v.get('interfaceCounters', 'N/A')
    if intf_counters != 'N/A':
      in_octets = intf_counters.get('inOctets')
      out_octets = intf_counters.get('outOctets')
    else:
      in_octets = 0
      out_octets = 0
    print "\n{:>15} {:>15} {:>15}".format(intf, in_octets, out_octets)
  print

if __name__ == "__main__":
  main()
