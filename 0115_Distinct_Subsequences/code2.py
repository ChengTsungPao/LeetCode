class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # 當s和t相等時，可選可不選，不相等時，只能尋找下一個s
            
        def recur(indexS, indexT, memo = {}):

            if (indexS, indexT) not in memo:
                
                if len(s) - indexS < len(t) - indexT:
                    return 0
                
                if indexT >= len(t):
                    return 1
                if indexS >= len(s):
                    return 0
                
                if s[indexS] == t[indexT]:
                    memo[indexS, indexT] = recur(indexS + 1, indexT + 1) + recur(indexS + 1, indexT)
                else:
                    memo[indexS, indexT] = recur(indexS + 1, indexT)

            return memo[indexS, indexT]
        
        return recur(0, 0)