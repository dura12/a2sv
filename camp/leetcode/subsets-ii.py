class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []
        def back(i , curr):
            if i <= len(nums):
                temp = curr.copy()
                temp.sort()
                if temp not in res:
                    res.append(temp)
            else:
                return
            for j in range(i , len(nums)):
                curr.append(nums[j])
                back(j + 1 , curr)
                curr.pop()

        back(0 , [])
        return res