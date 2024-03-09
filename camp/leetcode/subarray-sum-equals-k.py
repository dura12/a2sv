class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref={0:1}
        res=0
        curr=0
        for i in range(len(nums)):
            curr+=nums[i]
            diff=curr-k
            res+=pref.get(diff,0)
            pref[curr]=1+pref.get(curr,0)
        return res
            