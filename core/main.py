#!/usr/bin/python3

import numpy as np


class Board:
    """ The main board of table sudoku """

    def __init__(self) -> None:
        self.board = np.zeros((3, 3, 3, 3), dtype='int32') # main board of sudoku table
    
    def put_numbers(self):
        range_numbers = np.arange(1,10)
        for irow, row in enumerate(self.board):
            for icol, little_board in enumerate(row):
                random_numbers = np.random.default_rng().choice(range_numbers, (3,3), replace=False)
                self.board[irow, icol] = random_numbers
    
    def get_table(self) -> np.array:
        return self.board

    def fixing_table(self) -> None:
        """
        This method will fix some wrong numbers position table
        The roles of sudoku game says: in each ``little_board`` 
        should not be a number that count of that number in row, col, and little_table more than one
        so this method:
            checks the role game.
            then if the position of number is wrong, it will change it to zero(non).
        """
        for irow, row in enumerate(self.board):
            for icol, little_board in enumerate(row):
                for ielement, element in enumerate(little_board):
                    for inum, number in enumerate(element):
                        # get all horizontal numbers in this number positon
                        horizantal_numbers = self.board[irow, :, ielement, :]

                        # get all vertical numbers in this number positon
                        vertical_numbers = self.board[:, icol, :, inum]

                        # get count of (vertical and horizontal) numbers
                        count_num_in_horizantal = np.count_nonzero(horizantal_numbers == number)
                        count_num_in_vertical = np.count_nonzero(vertical_numbers == number)
                        
                        # if count of numbers more than one, then change it to zero(non)
                        if count_num_in_horizantal > 1 or count_num_in_vertical > 1:
                            self.board[irow, icol, ielement, inum] = 0
