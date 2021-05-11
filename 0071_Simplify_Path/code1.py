class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack, path = [], re.split("/+", path.strip("/"))

        for p in path:
            if stack and p == "..":
                stack.pop()
            if not (p == "." or p == ".."):
                stack.append("/" + p)
            
        return "/" * (stack == []) + "".join(stack)