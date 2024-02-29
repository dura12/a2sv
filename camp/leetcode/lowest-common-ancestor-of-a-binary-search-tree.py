# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        b = max(p.val,q.val)
        d = min(p.val,q.val)
        m = 10**9 + 7
        def smallest(node):
            nonlocal m
            if not node:
                return None
            if node.val >= d and node.val <= b:
                m = min(m , node.val)
            if node.val < d:
                smallest(node.right)
            if node.val > b:
                smallest(node.left)
            return TreeNode(m)
        return smallest(root)

        
        