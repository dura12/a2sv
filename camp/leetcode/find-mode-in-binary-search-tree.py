class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hash_map = {}
        
        def preorder(node):
            if not node:
                return
            hash_map[node.val] = hash_map.get(node.val, 0) + 1
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        
        m_count = max(hash_map.values())
        ans = [i for i, v in hash_map.items() if v == m_count]
        
        return ans