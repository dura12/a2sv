# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = ""
        stack = []
        res = []
        def dfs(node):

            nonlocal stack
            if not node:
                return
            stack.append(node.val)
            dfs(node.left)

            if not node.left and not node.right:
                s =""
                for i in stack:
                    s += str(i)
                res.append(s)
            dfs(node.right)
            stack.pop()
        dfs(root)
        sum_ = 0
        for i in res:
            sum_ += int(i)
        
        return sum_
        