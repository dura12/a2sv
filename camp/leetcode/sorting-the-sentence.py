class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        res = [0]*len(s)
        for i in s:
            m=int(i[-1])
            res[m-1] = i[:-1]
        print(res)
        return " ".join(res)
        