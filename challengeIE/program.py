#!/usr/bin/env python3

import sys

def bitcoin(coins):
    incl = 0
    excl = 0

    for i in coins:
        tmp = max(excl, incl)
        incl = excl + i
        excl = tmp

    return max(excl,incl)


def main():
    for line in sys.stdin:
        coins = list(map(int, line.strip().split()))
        print(bitcoin(coins))

if __name__ == '__main__':
    main()
