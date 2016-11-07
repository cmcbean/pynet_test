#!/usr/bin/env python


ip_addr = raw_input("Please enter the IP Address: ")
ip_addr2 = ip_addr.split(".")
ip_addr2[-1] = 0

ip_binary = []
ip_binary.append(bin(int(ip_addr2[0])))
ip_binary.append(bin(int(ip_addr2[1])))
ip_binary.append(bin(int(ip_addr2[2])))
ip_binary.append(bin(int(ip_addr2[3])))

print
print
print

print "{:<12} {:<12} {:<12} {:<12}".format('octet1', 'octet2', 'octet3', 'octet4')
print "{:<12} {:<12} {:<12} {:<12}".format(*ip_addr2)
print "{:<12} {:<12} {:<12} {:<12}".format(*ip_binary)

print
print
print
