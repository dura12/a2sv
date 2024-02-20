class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        c=0
        if maxDoubles==0:
            return target-1
        while True:
            if target ==1:
                break
            if target%2==0:
                if maxDoubles >0:
                    maxDoubles-=1
                    target=int(target/2)
                    c+=1 
                else:
                    return target -1 +c
            else:
            
                c+=1
                target-=1
        return c
        
    