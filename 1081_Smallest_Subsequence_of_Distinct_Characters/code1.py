class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        count = collections.Counter(s)
        visited = set()
        
        stack = []
        for ch in s:
            if ch in visited:
                count[ch] -= 1
                continue
            
            while stack and stack[-1] >= ch and count[stack[-1]] > 0:
                visited.remove(stack.pop())
            
            stack.append(ch)
            visited.add(ch)
            count[ch] -= 1

        return "".join(stack)