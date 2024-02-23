class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        res=[]
        m=set()
        prev={char:i for i , char  in enumerate(s)}
        for i , char in enumerate(s):
            if char not in m:
                while res and res[-1] > char and i < prev[res[-1]]:
                    m.discard(res.pop())
                m.add(char)
                res.append(s[i])
        return "".join(res)


                



        