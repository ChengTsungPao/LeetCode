class Solution:
    def checkRecord(self, n: int) -> int:
        
        MOD = 10 ** 9 + 7
        
        memo = {}
        def recur(day, A, L):
            
            if (day, A, L) not in memo:

                if A >= 2 or L >= 3:
                    return 0
                
                if day >= n:
                    return 1

                memo[day, A, L] = (recur(day + 1, A, 0) + recur(day + 1, A + 1, 0) + recur(day + 1, A, L + 1)) % MOD
            
            return memo[day, A, L]
        
        return recur(0, 0, 0)