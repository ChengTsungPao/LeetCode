class Solution:
    def longestPrefix(self, s: str) -> str:
        
        n = len(s)
        
        ans = ""
        subStr1 = subStr2 = 0
        powCache = 1
        MOD = 10 ** 7 + 1
        
        for i in range(n - 1):
            subStr1 = (26 * subStr1 + (ord(s[i]) - 26)) % MOD
            subStr2 = (subStr2 + (ord(s[~i]) - 26) * powCache) % MOD
            powCache = (powCache * 26) % MOD
            if subStr1 == subStr2:
                ans = s[:i + 1]
            
        return ans