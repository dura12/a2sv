class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        l = 0
        k = len(s1)
        s1_ = [0] * 26
        s2_ = [0] * 26
        for i in range(k):
            s1_[ord(s1[i]) - ord("a")] += 1
            s2_[ord(s2[i]) - ord("a")] += 1
        
        r = k
        while r < len(s2):
            if s1_ == s2_:
                return True

            s2_[ord(s2[l]) - ord("a")] -=1
            l += 1
            s2_[ord(s2[r]) - ord("a")] += 1
            r += 1

        return s1_ == s2_