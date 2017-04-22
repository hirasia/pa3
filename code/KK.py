import sys
import numpy as np
from bisect import insort_left

import helpers

def kk(nums):
	N = list(nums)
	N.sort()
	while len(N) > 1:
		insort_left(N, abs(N.pop() - N.pop()))
	return N[0]

if __name__ == '__main__':
	fname = sys.argv[1]
	nums = helpers.from_file(fname)
	print(kk(nums))
