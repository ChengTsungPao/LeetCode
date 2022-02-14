class Solution:
    def numDecodings(self, s: str) -> int:
        
        def recur(index, memo = {}):
            
            if index not in memo:
                
                if index == len(s):
                    return 1
                elif index > len(s) or s[index] == "0":
                    return 0
                
                ans = 0
                if int(s[index: index + 2]) <= 26:
                    ans += recur(index + 2)
                ans += recur(index + 1)
                
                memo[index] = ans
                
            return memo[index]
        
        return recur(0)