class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        status = {}
        for i in range(len(s)):
            status[s[i]] = i
            
        stack = [] 
        visited = set()
        
        for index in range(len(s)):
            ch = s[index]
            if ch in visited:
                continue
            
            while stack and ch < stack[-1] and index < status[stack[-1]]:
                visited.remove(stack.pop())
            stack.append(ch)
            visited.add(ch)
            
        return "".join(stack)