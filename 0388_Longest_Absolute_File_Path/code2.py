class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        def layer(s):
            level = 0
            while s[level] == "\t":
                level += 1                
            return level, s[level:]
        
        ans = 0
        stack = []
        for dirname in input.split("\n"):
            level, dirname = layer(dirname)
            
            if level >= len(stack):
                stack.append(dirname)
            else:
                stack = stack[:level + 1]
                stack[-1] = dirname

            if stack[-1].find(".") != -1:
                ans = max(ans, len("/".join(stack)))
        
        return ans