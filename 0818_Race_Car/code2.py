class Solution:
    def racecar(self, target: int) -> int:

        # 情況一 => 持續加速到超過target，再折返到target
        # 情況二 => 持續加速剛好會到target
        # 情況三 => 持續加速到將近target，再折返到某個位置，再加速到target
        
        def move(step):
            return 2 ** step - 1
        
        n = 1
        dp = [0] * (target + 1)
        
        for i in range(1, target + 1):
            if move(n) == i:
                dp[i] = n
                n += 1
            else:
                dp[i] = n + 1 + dp[move(n) - i]
                for j in range(n - 1):
                    dp[i] = min(dp[i], (n - 1 + 1) + (j + 1) + dp[i - (move(n - 1) - move(j))])
                    
        return dp[target]