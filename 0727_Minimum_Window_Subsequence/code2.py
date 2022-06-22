class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        
        m = len(s1)
        n = len(s2)
        
        if m < n:
            return ""
        
        dp = [(-1, -1)] * n
        index = (m, 2 * m)
        
        for k in range(m):
            i, j = k, 0
            if s1[i] != s2[j]:
                continue
            
            record = []
            while i < m and j < n:
                ch1, ch2 = s1[i], s2[j]
                
                if dp[j][0] >= i:
                    i, j = dp[j][1], n
                    break
                
                if ch1 == ch2:
                    record.append(i)
                    i += 1
                    j += 1
                else:
                    i += 1
            
            # Not found subsequence
            if j < n:
                break
            
            # Found subsequence update dp
            for j, r in enumerate(record):
                dp[j] = (r, i)
                
            index = min(index, (k, i), key = lambda x: (x[1] - x[0], x[0]))

        return s1[index[0]: index[1]]