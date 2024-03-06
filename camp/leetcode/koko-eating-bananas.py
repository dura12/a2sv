class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left , right , best = 1 , max(piles) , -1
        while left <= right:
            mid = (left + right)//2
            calculated_h = 0
            for i in range(len(piles)):
                calculated_h += ceil(piles[i]/mid)
            if calculated_h > h:
                left = mid + 1
                
            else:
                right = mid - 1
                best = mid
        return best

                
        