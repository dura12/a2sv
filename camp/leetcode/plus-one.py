class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        combined_number = int(''.join(map(str, digits)))
        combined_number=combined_number+1
        s=[int(i)for i in str(combined_number)]
        return s

