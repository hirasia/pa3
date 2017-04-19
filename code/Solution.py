import numpy as np
import KK

class Standard:
    """
    Standard solution representation class.
    """
    def get_rand(self, n):
        """Generate random solution of length `n`"""
        return np.random.choice([-1, 1], size=n)

    def get_neighbor(self, soln):
        """Get random neighbor of solution `soln`"""
        soln_ = np.copy(soln)

        # get random indices
        [i, j] = np.random.choice(len(soln), 2, replace=False)

        # move 1 element to opp. set with p = 1/2
        soln_[i] = -soln_[i]

        # swap 2 elements with p = 1/2
        if np.random.random_sample() > 0.5:
            soln_[j] = -soln_[j]

        return soln_

    def residue(self, soln, nums):
        """Get residue of solution `soln` on array `nums`"""
        return abs(soln.dot(nums))

    def to_partition(self, soln):
        """Convert solution in standard rep to partition rep"""
        return np.where(soln > 0, x=1, y=0)

class PrePartition:
    """
    PrePartition solution representation class.
    """
    def get_rand(self, n):
        """Generate random solution of length `n`"""
        return np.random.randint(n, size=n)

    def get_neighbor(self, soln):
        """Get random neighbor of solution `soln`"""
        n = len(soln)
        soln_ = np.copy(soln)

        # get random indices
        i = np.random.randint(n)
        j = soln_[i]
        while j == soln_[i]:
            j = np.random.randint(n)

        soln_[i] = j
        return soln_

    def to_nums(self, soln, nums):
        """Convert solution in partition rep to array"""
        n = len(soln)
        nums_ = np.zeros(n, dtype=np.int64)
        for i in range(n):
            nums_[soln[i]] += nums[i]
        return nums_

    def residue(self, soln, nums):
        """Get residue of solution `soln` on array `nums`"""
        return KK.kk(self.to_nums(soln, nums))

def main():
    """
    Testing classes.
    """
    n = np.ones(10)

    std = Standard()
    s = std.get_rand(10)
    r = std.residue(s, n)

    s_ = std.get_neighbor(s)
    r_ = std.residue(s_, n)

    print("Std\nS:  {} (r={})\nS': {} (r={})\n\n".format(s, r, s_, r_))

    pp = PrePartition()
    s = pp.get_rand(10)
    r = pp.residue(s, n)

    s_ = pp.get_neighbor(s)
    r_ = pp.residue(s_, n)

    print("PP\nS:  {} (r={})\nS': {} (r={})\n\n".format(s, r, s_, r_))


if __name__ == "__main__":
    main()
