class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        res=0
        char=set()
        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[l])
                l+=1
            char.add(s[r])
            res=max(res,len(char))
        return res





        