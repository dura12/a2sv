
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum=0
        def inorder(root):
            if root:
                if low < root.val:
                    inorder(root.left)
                if low <= root.val <= high:
                    self.sum+=root.val
                   
                if  high > root.val:
                    inorder(root.right)
        inorder(root)
        return self.sum