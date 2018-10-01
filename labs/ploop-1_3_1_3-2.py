#!/usr/bin/env python3
# script to ping a range of IP addresses
# uses netaddr for it's arbitrary range feature (built in IPAddress
# doesn't have this feature).  Uses subprocess to execute ping system
# command.

import subprocess
import argparse

import netaddr

DEVNULL = subprocess.DEVNULL
PIPE = subprocess.PIPE

p = argparse.ArgumentParser(description='Ping IPv4 addresses in the range start-end, inclusive; start & end are provided as parameters')
p.add_argument('start', help='Enter IP address range starting address')
p.add_argument('end', help='Enter IP address range ending address')

args = p.parse_args() #todo check values

range = netaddr.iter_iprange(args.start, args.end)

print('Begin ping sweep\n')

for addr in range:

  cmd = 'ping -c 1 {}'.format(addr)
  cmd = cmd.split()  # run() requires a list of command args, so using split()

  result = subprocess.run(cmd, stdout=PIPE)

  if b'bytes from' in result.stdout:  # stdout is a set of bytes
    
    print(addr)

