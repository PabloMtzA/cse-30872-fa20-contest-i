#!/usr/bin/env python3

import sys

SCORES = [2, 3, 7]
# OUT = []

def score(n, comb, out):
    if not comb:
        for a in SCORES:
            comb.append(a)
            score(n,comb,out)
            comb.pop()
    else:
        if sum(comb) >= n:
            if sum(comb) == n and not sorted(comb) in out:
                out.append(comb.copy())
                return
        else:
            if comb[-1] == 3:
                for i in range(1,len(SCORES)):
                    comb.append(SCORES[i])
                    score(n,comb,out)
                    comb.pop()
            elif comb[-1] == 7:
                    comb.append(7)
                    score(n,comb,out)
                    comb.pop()
            else:
                for a in SCORES:
                    comb.append(a)
                    score(n,comb,out)
                    comb.pop()

    return out

def main():
    for line in sys.stdin:
        n = int(line.strip())
        out = score(n,[],[])
        if len(out) == 1:
            print("There is %d way to achieve a score of %d:" %(len(out), n))
            print(' '.join(map(str, out[0])))
        else:
            print("There are %d ways to achieve a score of %d:" %(len(out), n))
            for a in out:
                print(' '.join(map(str, a)))

if __name__ == '__main__':
    main()
