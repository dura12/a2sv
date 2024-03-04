class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def track(i , cur): 
            if i <= len(nums):
                res.append(cur.copy())
            else:
                return
            for j in range(i ,len(nums)):
                cur.append(nums[j])
                track(j+1 , cur)
                cur.pop()
            
        track(0 , [])
        print(res)
        return res


        