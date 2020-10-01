#!/usr/bin/env python3

import sys

def isomorphic(s, t):
    seen = {}
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] in seen:
            if seen[s[i]] != t[i]:
                return False
        else:
            seen[s[i]] = t[i]

    return True

def main():
    for line in sys.stdin:
        strs = line.strip().split()
        if isomorphic(strs[0], strs[1]):
            print('Isomorphic')
        else:
            print('Not Isomorphic')

if __name__ == '__main__':
    main()
