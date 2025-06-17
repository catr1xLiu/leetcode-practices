from typing import *

class Sudoku:
    '''
    Whether each grid on the board can be modified.
    Grids that are initial provided in the problem are NOT modifiable.
    '''
    modifiable = []
    '''
    The current sudoku board.
    '''
    board = []

    '''
    Stack that contains the modification history
    Each item is in [x,y] format
    '''
    modify_stack = []

    cursor_x = 0
    cursor_y = 0

    def __init__(self, initial_board:List[List[str]]):
        '''
        Creates a new Sudoku puzzle
        '''
        for i in range(8):
            self.modifiable.append([])
            self.board.append([])
            for j in range(8):
                grid_val = initial_board[i][j]
                self.modifiable[i].append(grid_val != '.')
                if (grid_val) == '.':
                    self.board.append(None)
                else:
                    self.board.append(int(grid_val))
    
    def validate(self, position_x:int, position_y:int) -> bool:
        '''
        Validates a grid.
        Retunrs True if the grid is legal, False otherwise
        '''
        val = self.board[position_x][position_y]

        self.board[position_x][position_y] = None # mark as None to avoid self-counting
        # Check horizontal / vertical line:
        flag = True
        for i in range(8):
            if self.board[i][position_y] == val:
                flag = False
            if self.board[position_x][i] == val:
                flag = False
        
        # Check Small 3x3 Grid
        initial_x = int(position_x / 3) * 3
        initial_y = int(position_y / 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[initial_x + i][initial_y + j] == val:
                    flag = True
            
        self.board[position_x][position_y] = val
        return flag
    
    def next_grid(self) -> bool:
        '''
        Move the cursor to the next modifiable grid
        Returns: False if the current grid is the last, True otherwise
        '''
        if self.cursor_x == self.cursor_y == 0:
            return False
        self.cursor_x += 1
        if self.cursor_x > 7:
            self.cursor_x = 0
            self.cursor_y += 1
        
        if self.modifiable[self.cursor_x][self.cursor_y]:
            return True
        
        return self.next_grid()

    def iterate(self) -> bool:


    def solve(self):
        if self.modifiable[self.cursor_x][self.cursor_y]:
            self.next_grid()
        for i in range(1e7):
            
        

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pass