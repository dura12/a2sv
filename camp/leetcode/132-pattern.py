class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        max_ = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < max_:
                return True
            while stack and stack[-1] < nums[i]:
                max_ = stack[-1]
                stack.pop()
            stack.append(nums[i])
        return False