class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left = [-1]*len(s)
        right = [0]*len(s)
        plates = [0]*len(s)
        res = [0]*len(queries)
        prev = -1
        left[0] = -1 if s[0] != "|" else  0
        for i , val in enumerate(s):
            if  val == "|":
                left[i] = i 
            else:
                left[i] = left[i -1]
        right[-1] =   -1 if s[-1] != "|"  else 0

        for i in range(len(s)-2 , -1 , -1):
            if  s[i] == "|":
                right[i] = i 
            else:
                right[i] = right[i + 1]
        plates[0] = 1 if s[0] != "|"  else 0
        for i in range(1 , len(s)):
            if  s[i] == "*":
                plates[i] = plates[i - 1] + 1
            else:
                plates[i] = plates[i - 1]
        for  i in range(len(queries)):
            l = right[queries[i][0]]
            r = left[queries[i][1]]
            if l != -1 and r != -1 and r - l > 1 :
                res[i] = (plates[r] - plates[l])

        return res
        