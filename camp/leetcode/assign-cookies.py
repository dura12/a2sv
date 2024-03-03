class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c = 0
        l = 0
        m = 0
        g.sort()
        s.sort()
        while l < len(s):
            if s[l] >= g[m]:
                m+=1
                c += 1
            l += 1
            if m == len(g):
                break
        return c
        