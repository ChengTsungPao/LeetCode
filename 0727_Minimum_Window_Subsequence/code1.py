class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        
        m = len(s1)
        n = len(s2)
        
        if m < n:
            return ""
        
        index = (m, 2 * m)
        for k in range(m):
            i, j = k, 0
            if s1[i] != s2[j]:
                continue
            
            while i < m and j < n:
                if s1[i] == s2[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
                    
            if j == n:
                index = min(index, (k, i), key = lambda x: (x[1] - x[0], x[0]))
                
        return s1[index[0]: index[1]]