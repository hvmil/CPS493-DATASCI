#!/usr/bin/env python
"""mapper.py"""
import sys
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.split(',')
    # split the line into words
    week = line[0]
    print(week + ','+str(line[1:(len(line)-1)]))



