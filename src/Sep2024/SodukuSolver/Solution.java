package Sep2024.SodukuSolver;// https://leetcode.com/problems/sudoku-solver/

class Solution {
    public static void main(String[] args) {
        final char[][] board = new char[9][9];
        final String[] boardString = new String[] {
                "53..7....",
                "6..195...",
                ".98....6.",
                "8...6...3",
                "4..8.3..1",
                "7...2...6",
                ".6....28.",
                "...419..5",
                "....8..79",
        };

        for (int i = 0; i < 9; i++)
            board[i] = boardString[i].toCharArray();

        new Solution().solveSudoku(board);

        for (char[] charArray : board) {
            for (char c : charArray)
                System.out.print(c + " ");
            System.out.println();
        }
    }

    public void solveSudoku(char[][] board) {
        solveSudoku(board, 0, 0);
    }

    public boolean solveSudoku(char[][] board, int i, int j) {
        if (i >= 9)
            return solveSudoku(board, 0, j + 1);
        if (j >= 9)
            return true; // solution found

        System.out.println(i + " " + j);
        if (board[i][j] != '.')
            return solveSudoku(board, i + 1, j);

        for (char attempt : "123456789".toCharArray()) {
            final char originalChar = board[i][j];
            board[i][j] = attempt;
            if (validateGivenPoint(board, i, j))
                if (solveSudoku(board, i + 1, j))
                    return true;
            board[i][j] = originalChar;
        }
        return false;
    }

    /**
     * separates the inner grid that the point belongs to
     * 
     * @param board
     * @param pointI
     * @param pointJ
     * @return
     */
    private char[][] separateInnerGrid(char[][] board, int pointI, int pointJ) {
        char[][] innerGrid = new char[3][3];

        final int startI = (pointI / 3) * 3, startJ = (pointJ / 3) * 3;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                innerGrid[i][j] = board[i + startI][j + startJ];

        return innerGrid;
    }

    private boolean validateGivenPoint(char[][] board, int row, int col) {
        // validate the current colum and row
        for (int index = 0; index < 9; index++) {
            if (index != col && board[row][index] == board[row][col])
                return false;
            if (index != row && board[index][col] == board[row][col])
                return false;
        }

        // validate the current inner gird
        final int innerGridRow = row % 3, innerGridCol = col % 3;
        final char[][] innerGrid = separateInnerGrid(board, row, col);
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (innerGridRow != i && innerGridCol != j && innerGrid[i][j] == innerGrid[innerGridRow][innerGridCol])
                    return false;

        return true;
    }
}