class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = 0
        if len(nums) < 2:
            return nums[0]/k
        for i in range(k):
            sum_ += nums[i]
        avr = sum_ /k
        r = k
        l = 0
        while r < len(nums):
            sum_ -= nums[l]
            sum_ += nums[r]
            avr = max(sum_/k , avr)
            l += 1
            r += 1
        return avr
        
        