class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right , best = max(weights) , sum(weights) , -1
        while left <= right:
            mid = left + (right - left)//2
            counted_day = 1
            m = 0
            for i in range(len(weights)):
                m += weights[i]
                if m > mid:
                    counted_day += 1
                    m = weights[i]
            if counted_day > days:
                left = mid + 1
            else:
                right = mid - 1
                best = mid
        return best

            