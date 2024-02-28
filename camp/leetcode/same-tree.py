class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def solve(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return solve(p.left, q.left) and solve(p.right, q.right)
        
        return solve(p, q)        