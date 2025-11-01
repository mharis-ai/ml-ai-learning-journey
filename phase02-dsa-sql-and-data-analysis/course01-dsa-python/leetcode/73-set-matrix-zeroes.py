class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        first_row_track = any(matrix[0][j] == 0 for j in range(col))
        first_col_track = any(matrix[i][0] == 0 for i in range(row))

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if first_row_track:
            for j in range(col):
                matrix[0][j] = 0
        if first_col_track:
            for i in range(row):
                matrix[i][0] = 0