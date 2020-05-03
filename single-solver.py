from sudoku3 import solve_all, from_file

if __name__ == '__main__':

    #solve_all(from_file("mine.txt"), "mine", 0.0)
    #solve_all(from_file("weekly-unsolvable/sudokuwiki-weekly-unsolvable.txt"), "weekly-unsovalble", 0.0)
    solve_all(from_file("weekly-unsolvable/parsed.txt"), "weekly-unsovalble", 0.0)    

    
