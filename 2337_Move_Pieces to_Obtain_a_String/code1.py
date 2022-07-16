class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        start += "L"
        target += "L"
        
        n = len(start)
        
        i = j = 0
        while i < n and j < n:
            
            while start[i] == "_":
                i += 1
                
            while target[j] == "_":
                j += 1
                
            if start[i] == target[j] == "L" and i >= j:
                i += 1
                j += 1
            elif start[i] == target[j] == "R" and i <= j:
                i += 1
                j += 1
            else:
                return False
            
        return i == j