class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])
        new_mat=[[0]*row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                new_mat[j][i]=matrix[i][j]
        return new_mat