class Solution:
    def divisorGame(self, n: int) -> bool:
        
        def recur(n, who, memo = {}):
            
            if n not in memo:
            
                if n == 1:
                    return not who

                if who:
                    result = False
                    for i in range(1, n):
                        if n % i == 0:
                            result = result or recur(n - i, not who)

                        if result:
                            break
                else:
                    result = True
                    for i in range(1, n):
                        if n % i == 0:
                            result = result and recur(n - i, not who)

                        if result == False:
                            break
                            
                memo[n] = result if who else not result
            
            return memo[n] if who else not memo[n]

        return recur(n, True)