# generate a bank of hard puzzles

import time, random

from sudoku3 import *


def generate( showif=1.0):
    """Attempt to solve a sequence of grids. Report results.  
    When showif is a number of seconds, display puzzles that take longer.                                                 
    When showif is None, don't display any puzzles."""
    cutoff=0.02
    def time_solve(grid):
        start = time.process_time()
        values = solve(grid)
        t = time.process_time()-start
        ## Display puzzles that take long enough
        if showif is not None and t > showif:
            #display(grid_values(grid))
            print(grid)
            if values: display(values) 
            print ('(%.2f seconds)\n' % t)
            #if values == False: print('False values: wrong set up without a solution')
        return (t, solved(values))
    for i in range(10000):
        grid = random_puzzle()
        t, r = time_solve(grid)
        if ( t > cutoff and r):
            print('save',i,' time: ',int(t*100),t)
            filename= 'bank/puzzle%d.txt' % int(t*100)
            with open(filename,'a') as f:
                f.write(grid+'\n')


from multiprocessing import Pool

if __name__ == "__main__":
    with Pool(15) as p:
        p.map(generate,[1.2]*1000)
    print('done')
    #generate(showif=None)
