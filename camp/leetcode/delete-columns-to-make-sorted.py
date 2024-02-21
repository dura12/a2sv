
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        n = len(strs)
        m = len(strs[0])
        
        for col in range(m):
            for row in range(1, n):
                if strs[row][col] < strs[row - 1][col]:
                    count += 1
                    break
        
        return count