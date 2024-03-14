class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                top = matrix[i-1][j-1]
                if top!=matrix[i][j]:
                    return False
                
        return True