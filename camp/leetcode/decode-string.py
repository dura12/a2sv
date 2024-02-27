class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == "]":
                temp = []
                while stack and stack [-1] != "[":
                    temp.append(stack.pop())
                stack.pop()
                temp.reverse()
                d = []
                while stack and stack[-1].isdigit():
                    d.append(stack.pop())
                d.reverse()
                stack.append(  int("".join(d)) * "".join(temp))
            if s[i] == ']':
                continue
            stack.append(s[i])
        return "".join(stack)


