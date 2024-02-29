class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = (''.join(char for char in s if char.isalnum())).lower()
        if len(result)==2 and result[0] !=result[1] :
            return False
        else:
            start = 0
            end = len(result)-1
            while(start<end):
                if result[start]!=result[end]:
                    return False
                start+=1
                end-=1
            return True
                
            