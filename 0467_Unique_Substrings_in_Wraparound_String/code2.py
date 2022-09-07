class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        
        n = len(p)
        count = [0] * 26
        
        length = 0
        for i in range(n):
            if length == 0 or ord(p[i]) - ord(p[i - 1]) in {1, -25}:
                length += 1
            else:
                length = 1
                
            count[ord(p[i]) - ord("a")] = max(count[ord(p[i]) - ord("a")], length)
            
        return sum(count)