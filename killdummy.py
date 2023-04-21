#!/usr/bin/env python3
'''Kills the dummyfuji directory'''

import shutil

try:
    shutil.rmtree('/Users/mcavigli/Desktop/dummyfuji')
except FileNotFoundError:
    print("The directory does not exist")
