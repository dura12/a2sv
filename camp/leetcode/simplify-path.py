class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        res=""
        path = path.split("/")
        for i in path:
            if stack and i == "..":
                stack.pop()
            if i not in {"",".",".."}:
                stack.append(i)
    
        return "/" + "/".join(stack)
        
                


        