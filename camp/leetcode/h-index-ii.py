class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            if citations[0] != 0:
                return 1
            else:
                return 0

        right  = len(citations) - 1
        n = len(citations)
        ans = [0]
        left = 0
        best = 0
        while left <= right:
            mid = left + (right - left)//2
            if n - mid > citations[mid]:
                left = mid + 1
            else:
                right = mid - 1
                best = n - mid 
        return best

        

            

        