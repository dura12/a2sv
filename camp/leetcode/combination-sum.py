class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def back(curr):
            if sum(curr) > target:
                return
            if sum(curr) == target:
                x = curr[:]
                x.sort()
                if x not in ans:
                    ans.append(x)
                return
            for i in range(len(candidates)):
                curr.append(candidates[i])
                back(curr)
                curr.pop()
        back([])
        return ans
            
    


            
        