class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        nums_copy = nums[:]
        num= [nums.remove(item) for item in nums_copy if item==val]
    
       


        