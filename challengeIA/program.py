#!/usr/bin/env python3

import sys

def numBuildings(b):
    l = 0
    r = len(b) - 1
    max = 0
    ct = 0
    while l <= r:
        if b[r] > max:
            max = b[r]
            ct += 1
        r -= 1
    return ct

def main():
    for line in sys.stdin:
        b = list(map(int, line.strip().split()))
        print(numBuildings(b))

if __name__ == '__main__':
    main()
