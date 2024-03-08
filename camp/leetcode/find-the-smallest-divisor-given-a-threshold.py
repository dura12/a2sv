class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left , right , best = 1 , max(nums) , -1
        while left <= right:
            mid = left + (right - left )//2
            max_ = 0
            for i in nums:
                max_ += ceil(i/mid)
            if max_ > threshold:
                left = mid + 1
            else:
                right = mid - 1
                best = mid
        return best

        