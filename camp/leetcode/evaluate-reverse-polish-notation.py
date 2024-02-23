import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op = {'+','-','*','/'}
        for i in range(len(tokens)):
            if tokens[i] in op:
                op2 = stack.pop()
                op1 = stack.pop()
                if tokens[i]=="+":
                   stack.append(op1+op2)
                elif tokens[i]=="-":
                   stack.append(op1-op2)
                elif tokens[i]=="*":
                   stack.append(op1*op2)
                elif tokens[i]=="/":
                    s=op1/op2
                    if s < 0:
                        stack.append(ceil(s))
                    else:
                        stack.append(floor(s))
            else:
                stack.append(int(tokens[i]))
        return stack.pop()