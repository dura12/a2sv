from collections import defaultdict
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.winner = defaultdict(int)
        self.c = defaultdict(int)
        self.score_prev = {"score" : 0 , "person" : 0}
        self.timestamps = times
        for i in range(len(persons)):
            self.c[persons[i]] += 1
            if self.score_prev["score"] <= self.c[persons[i]]:
                self.score_prev["score"] = self.c[persons[i]]
                self.score_prev["person"] = persons[i]
                self.winner[self.timestamps[i]] = persons[i]
            else:
                self.winner[times[i]] = self.score_prev["person"]
    def q(self, t: int) -> int:
        l = 0 
        r = len(self.timestamps) - 1
        while l <= r :
            mid = l + (r - l ) // 2
            if self.timestamps[mid] > t :
                r = mid - 1
            else:
                l = mid + 1
        return self.winner[self.timestamps[r]]            

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)