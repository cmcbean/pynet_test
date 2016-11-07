#!/usr/bin/env python



ip_addr = raw_input("Please enter the IP Address: ")
ip_addr2 = ip_addr.split(".")

print
print
print

print "{:<12} {:<12} {:<12} {:<12}".format(*ip_addr2)

print
print
print
