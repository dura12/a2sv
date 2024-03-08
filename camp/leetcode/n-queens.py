class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        neg = set()
        pos = set()
        board = [["."]*n for _ in range(n)]
        res = []
        def back(row):
            if n == row:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if row - c in neg or  c in col or row + c in pos:
                    continue
                col.add(c)
                neg.add(row - c)
                pos.add(row + c)
                board[row][c] = "Q"
                back(row + 1)
                col.remove(c)
                neg.remove(row - c)
                pos.remove(row + c)
                board[row][c] = "."
        back(0)
        return res