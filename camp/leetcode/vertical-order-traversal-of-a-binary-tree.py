# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        res = []
        def traverse(node , row , col):
            nonlocal ans
            if not node:
                return 

            ans.append([col,row ,node.val])
            traverse(node.left , row + 1 , col - 1)
            traverse(node.right , row +1 , col + 1)
        traverse(root , 0 , 0)
        ans.sort()
        dictt = defaultdict(list)
        for col, row, val in ans:
            dictt[col].append(val)
        return dictt.values()

        