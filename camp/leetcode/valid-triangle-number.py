class Solution:
    def triangleNumber(self, nums):
        res = 0

        nums.sort()

        for i in range(2,len(nums)):
            low, high = 0, i-1 
            target = nums[i]

            while low < high:
                if nums[low] + nums[high] > target:
                    res += high - low 
                    high -= 1 
                else:
                    low += 1 

        return res


            
        