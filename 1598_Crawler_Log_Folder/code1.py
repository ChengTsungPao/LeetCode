class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []
        for folder in os.path.join(*logs).strip("/").split("/"):
            if folder == "..":
                if stack: stack.pop()
            elif folder == ".":
                pass
            else:
                stack.append(folder)
        
        return len(stack)