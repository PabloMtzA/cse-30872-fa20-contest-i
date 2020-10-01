#!/usr/bin/env python3

import sys

def permSwaps(n, k, i):
    ct = 0
    while k and ct < n:
        tmp = i.index(max(i[ct:n]))
        if tmp != ct:
            tmp = max(i[ct:n])
            i[i.index(max(i[ct:n]))] = i[ct]
            i[ct] = tmp
            k -= 1
        ct += 1

    return i

def main():
    for line in sys.stdin:
        N, K = line.strip().split()
        I = list(map(int, sys.stdin.readline().strip().split()))
        i = permSwaps(int(N),int(K),I)
        print(' '.join(map(str, i)))


if __name__ == '__main__':
    main()
