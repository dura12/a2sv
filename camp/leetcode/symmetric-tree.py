# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        val = True
        def com(node_l , node_r):
            if node_l == None and node_r == None:
                return True
            if not node_l or not node_r or node_l.val != node_r.val:
                return False
            return com(node_l.left,node_r.right) and com(node_l.right,node_r.left)
        return com(root , root)

            
            