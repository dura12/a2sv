class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        ans = []
        for key , val in dic.items():
            if val >1:
                ans.append(key)
        ans.sort()
        return ans
