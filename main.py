import sys
import logging
from typing import Optional

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit

from game.ui.sudoku_pazzle import Ui_Form 
from core.board import Board


class SudokuPazzle(QWidget):
    """ The Sudoku Pazzle Widget which you will play game """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        # Set the ui
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.reload_puzzle.clicked.connect(self.fill_pazzle_ui)
        
    
    def fill_pazzle_ui(self):
        self.board = Board()
        self.board.fill_puzzle() # filling the puzzle

        # get numbers/data :) finally
        puzzle = self.board.get_puzzle()
        
        # set the number in ui table
        for irow, row in enumerate(puzzle):
            for icol, col in enumerate(row):
                line_edit = self.get_item_puzzle_ui(irow, icol)
                if line_edit:
                    if col != 0:
                        line_edit.setText(str(col))
                        line_edit.setReadOnly(True)
                        line_edit.setStyleSheet('background-color:#5aea84;color:#fff')
                    else:
                        line_edit.setText("H")
                        line_edit.setReadOnly(False)
                        line_edit.setStyleSheet('background-color:#fff;color:#000')


    def get_item_puzzle_ui(self, irow: int = None, icol: int = None) -> Optional[QLineEdit]:
        """
            Return the specific item in the puzzle ui

            params:
                irow: index_row of self.board
                icol: index_column of self.board

            reslut:
                return getattr(self.ui, f'lineEdit_{irow}{icol}{ielement}{inumber}')
        """
        line_edit = getattr(self.ui, f'lineEdit_{irow}{icol}')
        if line_edit:
            return line_edit



if __name__ == '__main__': # Run the game
    app = QApplication(sys.argv)
    
    sudoku_pazzle = SudokuPazzle()
    sudoku_pazzle.fill_pazzle_ui()
    sudoku_pazzle.show()

    sys.exit(app.exec_())