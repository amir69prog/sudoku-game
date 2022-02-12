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

    def table_validation(self) -> None:
        """
        This method will some validation proccess for table
        The roles of sudoku game says: in each ``little_board`` 
        should not be a number that count of that number in row, col, and little_table more than one
        so this method:
            checks the role game.
            then will stores all numbers that count of them is more than one with theire positions 
        """

        for irow, row in enumerate(self.board):
            for icol, little_board in enumerate(row):
                for ielement, element in enumerate(little_board):
                    for inum, number in enumerate(element):
                        horizantal_numbers = self.board[irow, :, ielement, :]
                        vertical_numbers = self.board[:, icol, :, inum]
                        count_num_in_horizantal = np.count_nonzero(horizantal_numbers == number)
                        count_num_in_vertical = np.count_nonzero(vertical_numbers == number)
                        if count_num_in_horizantal > 1:
                            # count this num in horizantal line is more than one
                            print(number, f'horizantal:{count_num_in_horizantal}')
                        if count_num_in_vertical > 1:
                            # count this num in vertical line is more than one
                            print(number, f'vertical:{count_num_in_vertical}')

                        # So i have done this part of program
                        # actually i found the count of numbers in horizantal and vertical line
                        # and now i should replace the numbers
                        # that if i replaced them with other number everything should be alright :(
                        # so that is dificult part of this program



b1 = Board()
b1.put_numbers()
print(b1.get_table())
b1.table_validation()