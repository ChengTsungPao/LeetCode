class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        MOD = 10 ** 9 + 7
        
        memo = {}
        def recur(n, target):
            
            if (n, target) not in memo:
            
                if target < 0 or n == 0:
                    return 1 * (target == 0)

                ans = 0
                for i in range(1, k + 1):
                    ans += recur(n - 1, target - i)
                    ans %= MOD
                    
                memo[n, target] = ans
                
            return memo[n, target]
        
        return recur(n, target)