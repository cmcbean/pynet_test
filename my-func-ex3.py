#!/usr/bin/env python
  

def my_func(x, y, z=20):
   return x + y + z


my_list = [27, 13, 47]
my_dict = {
     'x': 17,
     'y': 7,
     'z': 2,
}

print
print

return_val = my_func(10, 20, 30)
print "Calling with three possitional arguments: {}".format(return_val)

print
print

return_val = my_func(x=10, y=20)
print "Calling function with two named arguments: {}".format(return_val)

print
print
return_val = my_func(10, z=13, y=20)
print "Calling function with one possitional and two named arguments: {}".format(return_val)

print
print
return_val = my_func(x='x', y='y', z='z')
print "Calling function with three strings: {}".format(return_val)

print
print

return_val = my_func(x=['x'], y=['y'], z=['z'])
print "Calling function with three lists: {}".format(return_val)

print
print

return_val = my_func(*my_list)
print "Calling function with *args: {}".format(return_val)

print
print

return_val = my_func(**my_dict)
print "Calling function with **kwargs: {}".format(return_val)

print
print


