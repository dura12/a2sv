class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def back(curr,i):
            if sum(curr) > target:
                return
            if sum(curr) == target:
                x = curr[:]
                x.sort()
                if x not in ans:
                    ans.append(x)
        
                return
            prev = -1
            for i in range(i , len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                back(curr,i+1)
                curr.pop()
                prev = candidates[i]
        back([],0)
        return ans