class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Initial: dp[k, k] = True
        # formula: dp[i, j] = s[i] == s[j] and dp[i + 1, j - 1]
        
        max_slice = 0, 0
        
        dp = [{(i, i): True for i in range(len(s))}, {}] # length = n + 1 and n
        
        for length in range(2, len(s) + 1):
            
            dp.insert(0, {})
            
            for index in range(len(s) - length + 1):
                
                i, j = index, index + length - 1
                
                if s[i] == s[j] and (dp[-1].get((i + 1, j - 1), False) or length == 2):
                    dp[0][i, j] = True
                    max_slice = i, j

            dp.pop()
            
            if dp == [{}, {}]:
                break
                    
        return s[max_slice[0]: max_slice[1] + 1]
     