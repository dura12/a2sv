# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def divide(n):
            if len(n) == 0:
                return
            mid = len(n)//2
            root = TreeNode(n[mid])
            root.left = divide(n[:mid])
            root.right = divide(n[mid + 1 :])
            return root

        return divide(nums)
        




            