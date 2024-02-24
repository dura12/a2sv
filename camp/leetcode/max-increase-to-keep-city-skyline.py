
import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max=[]
        ans=0
        total_sum = 0
        for row in grid:
            for element in row:
                total_sum += element
        for i in grid:
            row_max.append(max(i))
        col_max = [max(column) for column in zip(*grid)]
        for i in row_max:
            for j in col_max:
                ans+=(min(i,j))
        return ans - total_sum
        