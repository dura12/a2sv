
from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        s=Counter(answers)
        ans=0
        for an ,freq in s.items():
            ans+=(an + 1)* (((freq -1)//(an+1))+1)
        return ans

        