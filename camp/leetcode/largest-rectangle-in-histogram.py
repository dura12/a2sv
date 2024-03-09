class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] 
        mx = 0
        
        for idx, h in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                mx= max(mx, height * (idx - index))
                start = index
            stack.append((start, h))
            
        
        
        for idx, h in stack:
            mx = max(mx, h * (len(heights) - idx))
            
            
        return mx