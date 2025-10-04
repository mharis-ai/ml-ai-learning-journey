class Solution:
    def totalNQueens(self, n: int):
        self.result = 0
        chess = ["." * n for _ in range(n)]
        leftrow = [0] * n
        lowerDiagonal = [0] * (2 * n - 1)
        upperDiagonal = [0] * (2 * n - 1)

        def backtrack(col):
            if col == n:
                self.result += 1
                return
            for row in range(n):
                if(
                    leftrow[row] == 0 and
                    lowerDiagonal[row + col] == 0 and
                    upperDiagonal[n - 1 + (col - row)] == 0
                ):
                    chess[row] = chess[row][:col] + "Q" + chess[row][col + 1:]
                    leftrow[row] = 1
                    lowerDiagonal[row + col] = 1
                    upperDiagonal[n - 1 + (col - row)] = 1

                    backtrack(col + 1)

                    chess[row] = chess[row][:col] + "." + chess[row][col + 1:]
                    leftrow[row] = 0
                    lowerDiagonal[row + col] = 0
                    upperDiagonal[n - 1 + (col - row)] = 0

        backtrack(0)
        return self.result