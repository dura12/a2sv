class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(n, guess, k):
            s = 0
            c = 1
            for i in n:
                if s + i > guess:
                    s = 0
                    c += 1
                s += i
            return c > k
                

        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right)//2
            if check(nums, mid, k):
                left = mid + 1
            else:
                right = mid - 1

        return left




