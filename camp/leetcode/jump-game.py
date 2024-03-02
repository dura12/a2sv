class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        for i in range(len(nums)):
            if i > start:
                return False  
            start = max(start, i+nums[i])
        return True
        