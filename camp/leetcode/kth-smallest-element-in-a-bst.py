# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = []
        def inorder(node):
            nonlocal q
            if not node:
                return 
            inorder(node.left)
            q.append(node.val)
            inorder(node.right)
        inorder(root)
        return q[k-1]
        