class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i : j] in wordDict and dp[i]:
                    dp[j] = True
                    
        return dp[-1]