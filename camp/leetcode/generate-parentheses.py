class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def back(open , close , curr):
            if open == n and close ==n:
                temp = curr.copy()
                res.append("".join(temp))
                return
            if open < n:
                curr.append("(")
                back(open + 1 ,close , curr )
                curr.pop()
            if close < open:
                curr.append(")")
                back(open , close + 1 ,curr)
                curr.pop()
        back(1 , 0 ,["("])
        return res

            

            


        