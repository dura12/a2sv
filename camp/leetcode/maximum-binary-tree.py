# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(n):
            if len(n) == 0:
                return
            s = max(n)
            idx = n.index(s)
            root = TreeNode(n[idx])
            root.left = build(n[:idx])
            root.right = build(n[idx+1:])
            return root
        return build(nums)

        