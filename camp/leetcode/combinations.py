class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        num = [i+1 for i in range(n)]
        res = []
        def comb(curr ,i):
            if len(curr) == k :
                res.append(curr.copy())
                return 
            for i in range(i, n+1):
                curr.append(i)
                comb(curr , i + 1)
                curr.pop()
        comb([] , 1)
        return res
            
        
        