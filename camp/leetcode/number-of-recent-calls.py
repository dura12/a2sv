from collections import deque
class RecentCounter:

    def __init__(self):
        self.count=0
        self.q=deque()

        

    def ping(self, t: int) -> int:
        self.q.append(t)
        self.count += 1
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
            self.count -= 1
        return self.count
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)