class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        num = sorted(nums)
        return [num.index(x) for x in nums]