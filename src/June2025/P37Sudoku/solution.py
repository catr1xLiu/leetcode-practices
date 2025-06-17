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
        for i in range(9):
            self.modifiable.append([])
            self.board.append([])
            for j in range(9):
                grid_val = initial_board[i][j]
                self.modifiable[i].append(grid_val == '.')
                if (grid_val) == '.':
                    self.board[i].append(0)
                else:
                    self.board[i].append(int(grid_val))
    
    def validate(self, position_x:int, position_y:int) -> bool:
        '''
        Validates a grid.
        Retunrs: True if the grid is legal, False otherwise
        '''
        val = self.board[position_x][position_y]

        self.board[position_x][position_y] = 0 # mark as None to avoid self-counting
        # Check horizontal / vertical line:
        flag = True
        for i in range(9):
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
                    flag = False
            
        self.board[position_x][position_y] = val
        return flag
    
    def next_grid(self) -> bool:
        '''
        Move the cursor to the next modifiable grid
        Returns: False if the current grid is the last, True otherwise
        '''
        if self.cursor_x == self.cursor_y == 8:
            return False
        self.cursor_x += 1
        if self.cursor_x >= 9:
            self.cursor_x = 0
            self.cursor_y += 1
        
        if self.modifiable[self.cursor_x][self.cursor_y]:
            return True
        
        return self.next_grid()

    def previous_grid(self) -> bool:
        '''
        Move the cursor to the previous modifiable grid
        Returns: False if the current grid is the last, True otherwise
        '''
        if self.cursor_x == self.cursor_y == 0:
            return False
        self.cursor_x -= 1
        if self.cursor_x < 0:
            self.cursor_x = 8
            self.cursor_y -= 1
        
        if self.modifiable[self.cursor_x][self.cursor_y]:
            return True
        
        return self.previous_grid()

    def iterate(self) -> bool:
        '''
        Make an attempt to move to fill in the current grid and move to the next grid.
        If it is impossible to fill the current grid, trace back to the previous grid.
        Returns False if the last modifiable grid is filled, marking the puzzle as complete; Returns True otherwise.
        '''
        # Increase (Create) the block value
        self.board[self.cursor_x][self.cursor_y] += 1

        # If the current value is greater than 9
        if self.board[self.cursor_x][self.cursor_y] > 9:
            self.board[self.cursor_x][self.cursor_y] = 0
            if not self.previous_grid():
                raise RuntimeError(f"Cannot TraceBack from {self.cursor_x}, {self.cursor_y}.")
            return True
        # If the attempt successeded
        if self.validate(self.cursor_x, self.cursor_y):
            return self.next_grid()
        return True

    def solve(self):
        if not self.modifiable[self.cursor_x][self.cursor_y]:
            self.next_grid()
        while self.iterate():
            pass
    
    def print(self):
        for i in self.board:
            print(i)
        print()

    def output(self, target:List[List[str]]):
        for i in range(9):
            for j in range(9):
                target[i][j] = str(self.board[i][j])
                target[i][j] = target[i][j].replace("0", ".")
        

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        sudoku = Sudoku(board)
        sudoku.solve()
        sudoku.output(board)
        sudoku.print()

if __name__ == '__main__':
    s = Solution()
    s.solveSudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]])
    
