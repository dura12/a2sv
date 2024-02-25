from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        col = len(mat[0])
        row = len(mat)
        lis = []

        for k in range(row + col - 1):
            temp = []
            if k < row:
                i = k
                j = 0
            else:
                i = row - 1
                j = k - (row - 1)
            
            while i >= 0 and j < col:
                temp.append(mat[i][j])
                i -= 1
                j += 1
            
            if k % 2 != 0:
                temp.reverse()
                
            lis += temp

        return lis