class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lis = [(position[i], speed[i]) for i in range(len(position))]
        lis.sort()
        for i in range(len(position)):
            lis[i] = ((target - lis[i][0]) / lis[i][1])
        stack = [lis[0]]
        print(lis)
        for i in range(1, len(lis)):
            if lis[i] < stack[-1]:
                stack.append(lis[i])
            else:
                while stack and stack[-1] <= lis[i]:
                    stack.pop()
                stack.append(lis[i])
        return len(stack)