class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right , idx = 0 , len(nums) - 1 , 0
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
        