# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lis = []
        def inorder(node):
            if not node:
                return 
            node.left = inorder(node.left)
            lis.append(node.val)
            node.left = inorder(node.right)
        inorder(root)
        def divide(n):
            if len(n) == 0:
                return
            mid = len(n)//2
            root = TreeNode(n[mid])
            root.left = divide(n[:mid])
            root.right = divide(n[mid + 1 :])
            return root

        return divide(lis)
        