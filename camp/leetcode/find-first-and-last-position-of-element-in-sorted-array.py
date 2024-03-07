
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right  = 0, len(nums)-1 
        ans = [-1, -1]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid -1
            elif nums[mid] < target:
                left = mid + 1

        if left >= len(nums) or nums[left] != target:
            return ans

        ans[0] = left
        right = len(nums)-1
        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid -1
            elif nums[mid] <= target:
                left = mid + 1
        ans[1] = right

        return ans

    

        
            
        
