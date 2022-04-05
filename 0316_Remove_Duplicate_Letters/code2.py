class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # 將大的字母往高位數推 (smallest lexicographical)
        
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        stack = []
        visited = set()
        for index in range(len(s)):
            ch = s[index]
            if ch in visited:
                continue
            
            while stack and ch < stack[-1] and lastIndex[stack[-1]] > index:
                visited.remove(stack.pop())
                
            visited.add(ch)
            stack.append(ch)
            
        return "".join(stack)