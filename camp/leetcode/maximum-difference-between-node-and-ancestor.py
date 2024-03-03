class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        stack = []
        ans = 0
        def inorder(node):
            nonlocal ans
            if not node:
                return 
            stack.append(node.val)
            inorder(node.left)
            if not node.left and not node.right:
                temp = stack.copy()
                temp.sort()
                if len(temp) >= 2:
                    ans = max( ans ,abs(temp[-1] - temp[0]))
            inorder(node.right)
            stack.pop()
        inorder(root)
        return ans
            

