class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 or k == 1:
            return 0
        
        left = 0
        right = 2**(n - 1)
        best = 0
        for i in range(n - 1):
            while left < right:
                mid = (left + right)//2
                if mid < k :
                    left = mid + 1 
                    best = 0 if best else 1 
                    
                else:
                    right = mid
                    
                    

                    
                
            
        return best

                