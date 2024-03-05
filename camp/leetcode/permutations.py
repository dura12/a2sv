
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        res = []
        def back(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return 
            for i in nums:
                if i in curr:
                    continue
                curr.append(i)
                back(curr)
                curr.pop()
        back([])
        return res