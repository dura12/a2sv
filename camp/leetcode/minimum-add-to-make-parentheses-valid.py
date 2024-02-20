from collections import Counter
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        prev={}
        open=0
        close=0
        count=0
        for i in s:
            if i=="(":
                open+=1
            if i ==")":
                if open >0:
                   open-=1
                else:
                     count+=1
        return open + count + close
                
                
        
        