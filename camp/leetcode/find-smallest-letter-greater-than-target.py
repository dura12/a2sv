class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left , right , found = 0 , len(letters) - 1 , letters[0]
        while left <= right:
            mid = (left + right)//2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
                found = letters[mid]
        return found
