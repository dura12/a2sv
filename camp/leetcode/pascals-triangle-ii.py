class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        mat = [[1] * (rowIndex+1) for _ in range(rowIndex+1)]
        for i in range(rowIndex +1):
            for j in range (i+1):
                if i == j or i == 0 or j == 0:
                    continue
                else:
                    mat[i][j] = mat[i-1][j -1] + mat[i-1][j] 
        return mat[rowIndex]

                
        
        
    

            