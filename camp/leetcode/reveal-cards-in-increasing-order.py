class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        m = sorted(deck)
        q = deque([i for i in range(len(m))])
        res = [0] * len(m)
        t = 0
        while q:
            top = q.popleft()
            res[top] = t
            t += 1
            if q:
                top = q.popleft()
                q.append(top)
        ans = []
        for i in res:
            ans.append(m[i])
        return ans
            
