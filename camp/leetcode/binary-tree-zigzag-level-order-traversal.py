from collections import deque
from typing import Optional, List

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            temp = [] 
            level_length = len(queue)

            for _ in range(level_length):
                node = queue.popleft()
                temp.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(temp)
        for i in range(len(res)):
            if i % 2 != 0:
                res[i].reverse()


        return res