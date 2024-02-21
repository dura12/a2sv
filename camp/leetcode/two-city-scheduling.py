class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s= sorted(costs, key=lambda x: x[0]-x[1])
        sum_=0
        m=int(len(costs)/2)
        for i in range(m):
            sum_+=s[i][0]
        for i in range(m,len(costs)):
            sum_+=s[i][1]

        return(sum_)