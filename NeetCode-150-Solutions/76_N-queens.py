"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard so
that no two queens can attack each other.

A queen in a chessboard can attack horizontally, vertically, and diagonally.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a unique board layout where the queen pieces are placed.
'Q' indicates a queen and '.' indicates an empty space.

You may return the answer in any order.
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(colMap, mainDiagMap, antiDiagMap, sol, row):
            if all(len(row) == n for row in sol) and len(sol) == n:
                res.append(sol.copy())
                return

            # iterating over the columns
            for col in range(0, n):
                # trying to assign current cell a queen
                if col not in colMap and not (row - col) in mainDiagMap and (row + col) not in antiDiagMap:
                    rowStr = '.' * col + 'Q' + '.' * (n - col - 1)
                    sol.append(rowStr)

                    mainDiagMap[row - col] = True
                    antiDiagMap[row + col] = True
                    colMap[col] = True

                    # explore
                    dfs(colMap, mainDiagMap, antiDiagMap, sol, row + 1)

                    # backtrack
                    sol.pop()

                    del mainDiagMap[row - col]
                    del antiDiagMap[row + col]
                    del colMap[col]

        dfs({}, {}, {}, [], 0)
        return res
