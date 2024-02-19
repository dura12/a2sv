class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        #return the numbers of oaurs(i,j) conditions 0< i<j<n and  nums[i] == nums[j] and (i * j) is divisible by k.
        # count=0
        #iterate through each elements with array
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and (i*j)%k==0:
                    count+=1
        return count

