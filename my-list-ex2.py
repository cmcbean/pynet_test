#!/usr/bin/env python

a_list = range(5)
a_list.append('1st added item')
a_list.append('2nd added item')

print a_list.pop(0)

print "Lenght of a list: {}".format(len(a_list))

a_list.sort()

print a_list

