class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        chance = 0
        l = 0
        r = 0
        count = 0
        track = 0
        deleted = 0

        while r < len(nums):
            if nums[r] == 1:
                r += 1
                count += 1
            elif nums[r] == 0 and chance == 0:
                r +=1
                chance = 1
                deleted = 1
            else:
                if nums[l] == 0:
                    chance = 0
                    deleted = 0
                count -=  nums[l]
                l += 1
            track = max(track ,count)
        if deleted:
            return track
        else:
            return track - 1     
           