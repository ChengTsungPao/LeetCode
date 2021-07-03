class Solution:
    def minCut(self, s: str) -> int:

        def recur(startindex, memo = {}):
            if startindex not in memo:
                if startindex == len(s):
                    return 0
                layer = float("inf")
                for i in range(startindex, len(s)):
                    sub_str = s[startindex:i + 1]
                    if sub_str == sub_str[::-1]:
                        layer = min(layer, recur(i + 1) + 1)
                memo[startindex] = layer
            return memo[startindex]
        
        return recur(0) - 1   
