import random
import numpy as np
from numpy.typing import ArrayLike

class Board:
    """ The main board of sudoku puzzle """

    def __init__(self) -> None:
        self.puzzle = np.zeros((9, 9), dtype='int32')
        self.numberList = [1,2,3,4,5,6,7,8,9]
    
    def fill_puzzle(self) -> bool:
        """
            This method will fill the puzzle with correct numbers
            There is no parameter for this method.
            when you call this method each time it will fill the puzzle with another random numbers
        """

        for i in range(81):
            row = i // 9
            col = i % 9
            if self.puzzle[row, col] == 0:
                random.shuffle(self.numberList)
                for value in self.numberList:
                    if not(value in self.puzzle[row]):
                        if not value in (self.puzzle[:, col]):
                            square = []
                            if row < 3:
                                if col < 3:
                                    square = [self.puzzle[i, 0:3] for i in range(0,3)]
                                elif col < 6:
                                    square = [self.puzzle[i, 3:6] for i in range(0,3)]
                                else:  
                                    square = [self.puzzle[i, 6:9] for i in range(0,3)]
                            elif row < 6:
                                if col < 3:
                                    square = [self.puzzle[i, 0:3] for i in range(3,6)]
                                elif col < 6:
                                    square = [self.puzzle[i, 3:6] for i in range(3,6)]
                                else:  
                                    square = [self.puzzle[i, 6:9] for i in range(3,6)]
                            else:
                                if col < 3:
                                    square = [self.puzzle[i, 0:3] for i in range(6,9)]
                                elif col < 6:
                                    square = [self.puzzle[i, 3:6] for i in range(6,9)]
                                else:  
                                    square = [self.puzzle[i, 6:9] for i in range(6,9)]
                            
                            combine_square = np.hstack((square[0],square[1],square[2]))
                            if not value in (combine_square):
                                self.puzzle[row, col] = value
                                if self.check_puzzle():
                                    return True
                                else:
                                    if self.fill_puzzle():
                                        return True
                            
                break
        self.puzzle[row][col] = 0

    def check_puzzle(self):
        """
            Checks the puzzle if that is correct. it means all numbers must have been filled
        """

        for row in range(0, 9):
            for col in range(0, 9):
                if self.puzzle[row, col] == 0:
                    return False
        return True
    
    def get_puzzle(self) -> ArrayLike:
        """ Just return the puzzle """

        return self.puzzle