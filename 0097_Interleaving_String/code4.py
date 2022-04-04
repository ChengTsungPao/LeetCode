class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        length1 = len(s1)
        length2 = len(s2)
        length3 = len(s3)
        
        if length1 + length2 != length3:
            return False
        
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        for i in range(length1, -1, -1):
            for j in range(length2, -1, -1):
                if i + j >= length3:
                    dp[i][j] = True
                else:
                    ans = False
                    if i < length1 and s1[i] == s3[i + j]:
                        ans = ans or dp[i + 1][j]
                    if j < length2 and s2[j] == s3[i + j]:
                        ans = ans or dp[i][j + 1]
                    dp[i][j] = ans
                    
        return dp[0][0]