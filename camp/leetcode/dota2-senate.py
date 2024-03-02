from collections import Counter
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = deque()
        d_queue = deque()
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)
        while r_queue and d_queue:
            r_index = r_queue.popleft()
            d_index = d_queue.popleft()
            if r_index < d_index:
                r_queue.append(r_index + n)
            else:
                d_queue.append(d_index + n)
        if r_queue:
            return "Radiant"
        return "Dire"


