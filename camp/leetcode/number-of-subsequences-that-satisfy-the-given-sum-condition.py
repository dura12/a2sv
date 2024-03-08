class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        def binary(num):
            left = 0 
            right =(len(nums)) - 1
            while left <= right:
                mid = left + (right - left ) // 2
                if nums[i] + nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid -1
            return right

        for i in range(len(nums)):
            if nums[i] * 2 <= target:
                ans += 2**(binary(nums[i]) - i)
            else:
                break    
            
        return ans % (10**9 + 7)




        