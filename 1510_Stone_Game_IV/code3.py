class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        # recur(n, who) => n開始who是否會贏，會的話回傳who
        
        memo = {}
        def recur(n, who):
            
            if n not in memo:
            
                if n == 0:
                    return not who
                elif n == 1:
                    return who

                if who:
                    ret = False
                    for i in range(1, int(n ** 0.5) + 1):
                        ret = ret or recur(n - i ** 2, not who)
                else:
                    ret = True
                    for i in range(1, int(n ** 0.5) + 1):
                        ret = ret and recur(n - i ** 2, not who)    
                        
                memo[n] = ret if who else not ret
                    
            return memo[n] if who else not memo[n]
        
        return recur(n, True)