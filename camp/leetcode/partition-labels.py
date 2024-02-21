class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        from collections import defaultdict
        prev={}
       
        for i in range(len(s)):
            prev[s[i]]=i
        lis=[]

        a=0
        start=0
        for i in range(len(s)):
            a=max(a,prev[s[i]])
            if a==i:
                x=(a+1)-start
                lis.append(x)
                start=a+1
                a=0
        return lis