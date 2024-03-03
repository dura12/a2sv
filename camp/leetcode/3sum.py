from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r=[]
        nums.sort()
        for i in range(len(nums)):
            if i >0 and nums[i-1]==nums[i]:
                continue
            start=i+1
            end=len(nums)-1
            while(start < end):
                if nums[i] + nums[start]+ nums[end] ==0:
                    r.append([nums[i],nums[start],nums[end]])
                    start+=1
                    while nums[start]==nums[start-1] and start <end:
                        start+=1
                elif nums[i] + nums[start]+ nums[end] > 0:
                    end-=1
                else:
                    start+=1
        return r














