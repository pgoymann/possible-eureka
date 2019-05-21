#!/usr/bin/env python

import argparse
#Philipp was here!
parser = argparse.ArgumentParser(description='An example python script, ready for extensions.')
parser.add_argument('--jens', action = 'store_true')
args = parser.parse_args()
parser-add_argument('--philipp', action = 'store_true')
print("Hello, Loosolab!")

if(args.jens):
    print("Hello, Jens!")
if(args.philipp):
    print('Hello Philipp')
