#!/usr/bin/env python3

import sys

out = []

def triplets(nums):

    out = []
    
    i = 0

    while i < (len(nums) - 2):
        first = nums[i]
        l = i+1
        r = len(nums) - 1
        while l < r:
            sum = first + nums[l] + nums[r]
            if sum == 0:
                out.append([first, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1]:
                    l += 1
            elif sum > 0:
                r -= 1
            else:
                l += 1

        while nums[i] == nums[i + 1] and i < (len(nums) - 2):
            i += 1
        i += 1
    return out



def main():
    first = 1
    for line in sys.stdin:
        if first:
            first = 0
        else:
            print('')
        nums = list(map(int, line.strip().split()))
        out = triplets(sorted(nums))
        for a in out:
            print(' + '.join(map(str, a)))

if __name__ == '__main__':
    main()
