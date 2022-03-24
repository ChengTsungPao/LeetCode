class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        # recur(n) => n開始是否會贏，會的話回傳True
        
        memo = {}
        def recur(n):
            
            if n not in memo:
            
                if n == 0:
                    return False
                elif n == 1:
                    return True

                ret = False
                for i in range(1, int(n ** 0.5) + 1):
                    ret = ret or not recur(n - i ** 2)  
                        
                memo[n] = ret
                    
            return memo[n]
        
        return recur(n)