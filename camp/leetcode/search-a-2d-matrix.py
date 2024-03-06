class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                continue
            left , right = 0 , len(matrix[0]) -1
            while left <= right:
                mid = (left + right)//2
                if matrix[i][mid] == target:
                    return True
                if matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False
        