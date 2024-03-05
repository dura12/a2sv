class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic1 = {}
        dic2 = {}
        if len(s) < len(p):
            return []
        res = []
        for i in range(26):
            dic1[chr(97 + i)] = 0
            dic2[chr(97 + i)] = 0
        for i in p:
            dic2[i] += 1
        for i in range(len(p)):
            dic1[s[i]] += 1
        if dic1 == dic2:
            res.append(0)
        l = 0
        r = len(p)
        while r < len(s):
            dic1[s[l]] -= 1
            dic1[s[r]] += 1
            if dic1 == dic2:
                res.append(l+1)
            r += 1
            l += 1
        print(res)
        return res

        

        