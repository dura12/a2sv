from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q=deque()
        max_q = deque()
        start = 0
        end = 0
        ans=0
        while end < len(nums) and start <=end:
            while min_q and min_q[-1] > nums[end]:
                min_q.pop()
            while max_q and max_q[-1] < nums[end]:
                max_q.pop()
            min_q.append(nums[end])
            max_q.append(nums[end])
            while max_q[0] - min_q[0] > limit:
                if nums[start] == min_q[0]:
                    min_q.popleft()
                if nums[start] == max_q[0]:
                    max_q.popleft()
                start+=1
            ans=max(ans , end - start + 1)
            end += 1
        return ans    
            




        



        
        