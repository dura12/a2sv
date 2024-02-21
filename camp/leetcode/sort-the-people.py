class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        prev = list(zip(heights, names))
        prev.sort(reverse=True)
        ans=[a[1] for a in prev]
        return ans
        