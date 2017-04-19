import sys
import numpy as np
import heapq

import helpers

def kk(nums):
    neg_nums = list(-nums)
    heapq.heapify(neg_nums)
    for _ in range(len(nums)-1):
        n1 = heapq.heappop(neg_nums)
        n2 = heapq.heappop(neg_nums)
        heapq.heappush(neg_nums, n1 - n2)
    return abs(neg_nums[0])

if __name__ == '__main__':
    fname = sys.argv[1]
    nums = helpers.from_file(fname)
    print(kk(nums))
