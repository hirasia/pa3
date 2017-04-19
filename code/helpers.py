import numpy as np

MIN_INT = 1
MAX_INT = 10 ** 12
N_INTS = 100

def get_rand_example(n):
    return np.random.randint(MIN_INT, high=MAX_INT + 1, size=n)

def from_file(fname):
    return np.array([int(line) for line in open(fname)])

def to_file(nums, fname):
    with open(fname, 'w') as f:
        for n in nums:
            print(n, file=f)

if __name__ == '__main__':
    test_file = 'nums.txt'
    nums = get_rand_example(N_INTS)
    to_file(nums, test_file)
    assert(np.array_equal(nums, from_file(test_file)))
