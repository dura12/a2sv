class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0]*len(height)
        right = [0]*len(height)
        ans = 0
        for i in range(1 , len(height)):
            left[i] = max(left[i-1] , height[i-1])
        for i in range(len(height)-2 , -1 , -1):
            right[i] = max(right[i+1] , height[i+1])
        print(left , right)
        for i in range(len(height)):
            s = min(left[i] , right[i])
            res = s - height[i]
            if res > 0:
                ans += res
        
        

        return ans
        