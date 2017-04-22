import numpy as np
import sys
import time

import Solution as S
import Heuristics as HT
import KK
import helpers

def run_exp(residue_file, time_file, n_exp=100, n_iter=25000, n=100):
    reps = [S.Standard(), S.PrePartition()]
    cols = ['KK', 'S_RR', 'S_HC', 'S_SA', 'P_RR', 'P_HC', 'P_SA']

    # residue matrix
    residues = -np.ones((n_exp, len(cols)), dtype=np.int64)

    # runtime matrix
    runtimes = np.zeros((n_exp, len(cols)))

    with open(residue_file, 'w') as rf:
        with open(time_file, 'w') as tf:
            # write header row to outfile
            for f in [rf, tf]:
                print(' & '.join(cols), end=' \\\\ \n', file=f)

            # run experiments
            for i in range(n_exp):
                if i % 10 == 0 :
                    print('exp {} / {}...'.format(i, n_exp))

                # generate new example of length `n`
                nums = helpers.get_rand_example(n)

                # karmarker-karp solution
                t0 = time.clock()
                residues[i, 0] = KK.kk(nums)
                runtimes[i, 0] = time.clock() - t0

                # heuristic solutions
                for j, rep in enumerate(reps):
                    start = rep.get_rand(n)

                    t0 = time.clock()
                    residues[i, 3*j+1] = HT.rr(nums, start, rep, n_iter)
                    runtimes[i, 3*j+1] = time.clock() - t0

                    t0 = time.clock()
                    residues[i, 3*j+2] = HT.hc(nums, start, rep, n_iter)
                    runtimes[i, 3*j+2] = time.clock() - t0

                    t0 = time.clock()
                    residues[i, 3*j+3] = HT.sa(nums, start, rep, n_iter)
                    runtimes[i, 3*j+3] = time.clock() - t0

                # write residues to outfile
                res = [str((r)) for r in residues[i]]
                print(' & '.join(res), end=' \\\\ \n', file=rf)

                # write runtimes to outfile
                times = ['{:.6f}'.format(t) for t in runtimes[i]]
                print(' & '.join(times), end=' \\\\ \n', file=tf)


            # write mean stats to outfile
            rstats = [str(int(m)) for m in np.mean(residues, axis=0)]
            print(' & '.join(rstats), file=rf)

            tstats = ['{:.6f}'.format(m) for m in np.mean(runtimes, axis=0)]
            print(' & '.join(tstats), file=tf)

    # print summary
    print('Mean residue, runtime for {} experiments:'.format(n_exp))
    for name, rmean, tmean in zip(cols, rstats, tstats):
        print('{}: res = {}, tm = {}'.format(name, rmean, tmean))


if __name__ == '__main__':
    # get results for part 2
    run_exp('residues_.txt', 'times_.txt')
