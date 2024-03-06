import bisect
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i,n in enumerate(intervals):
            n.append(i)
        intervals.sort()
        result = [-1]*len(intervals)
        first = [s for s , e , i in intervals]
        for start , end , idx in intervals:
            x = bisect.bisect_left(first , end)
            if x != len(first):
                result[idx] = intervals[x][-1]
        return result