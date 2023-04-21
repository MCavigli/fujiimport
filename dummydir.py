#!/usr/bin/env python3
'''A simple script that makes a dummy folder for testing'''
import os
import sys
import killdummy

try:
    os.mkdir('/Users/mcavigli/Desktop/dummyfuji')
    print("File made")
except FileExistsError:
    print("File already exists. Killing directory, then remaking...")
    killdummy()

os.mkdir('/Users/mcavigli/Desktop/dummyfuji/JPG/')
os.mkdir('/Users/mcavigli/Desktop/dummyfuji/RAW/')

try:
    os.mkdir('/Users/mcavigli/Desktop/dummyDCIM')
except FileExistsError:
    print("dummyDCIM folder already exists")

DCIMpath = '/Users/mcavigli/Desktop/dummyDCIM'
jpgpath = '/Users/mcavigli/Desktop/dummyfuji/JPG/'
rawpath = '/Users/mcavigli/Desktop/dummyfuji/RAW/'

for i in range(10):
    jpgfile = os.path.join(DCIMpath, f"file_{i}.jpg")
    rawfile = os.path.join(DCIMpath, f"file_{i}.raf")
    with open(jpgfile, "w"):
        pass
    with open(rawfile, "w"):
        pass
print("Files created")
