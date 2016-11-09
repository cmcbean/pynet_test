#!/usr/bin/env python


from netmiko import ConnectHandler
import yaml

def read_yml_file(filename):
    """Read YAML File"""
    with oen(filename) as f:
      return yaml.load(f)


def main():
    file_name = 'my-yaml-ex1.yml'
    a_device = read_yml_file(file_name)
    print a_device

    netmi

 

