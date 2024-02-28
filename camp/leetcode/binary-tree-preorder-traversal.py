# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre(self,root ,ans):
        if root == None:
            return ans
        ans.append(root.val)
        self.pre(root.left , ans)
        self.pre(root.right , ans)
    

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.pre(root , ans)
        return ans

        