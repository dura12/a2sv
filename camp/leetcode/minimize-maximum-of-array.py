class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        max_ = max(nums)
        if nums[0] == max_:
            return nums[0]
        sum_ = 0
        res=0
        for i in range(len(nums)):
            sum_ += nums[i]
            avr = ceil(sum_/(i+1))
            res=max(res,avr)
        return res



               
                