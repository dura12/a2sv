# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxd(root , l):
            if root == None:
                return l
            ans = maxd(root.left, l+1)
            ans2 = maxd(root.right, l+1)
            m = max(ans , ans2)
            return m
        return maxd(root , 0)

         
        

        