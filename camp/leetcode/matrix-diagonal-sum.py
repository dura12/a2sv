class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            for j in range ( len(mat[0])):
                if i == j:
                    ans += mat[i][j]
        k = len(mat) - 1
        for i in range(len(mat)):
            if k != i:
                ans += mat[i][k]
            k -= 1
        return ans

                
                

        