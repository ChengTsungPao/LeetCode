class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        '''
        Recursion
            index => 0 ~ n
        '''
        
        n = len(stoneValue)
        dp = [0] * (n + 1)
        
        for index in range(n, -1, -1):
            if index >= n:
                dp[index] = 0
            else:
                ans = -float("inf")
                for i in range(1, 3 + 1):
                    if index + i >= n:
                        ans = max(ans, sum(stoneValue[index: index + i]) - 0)
                    else:
                        ans = max(ans, sum(stoneValue[index: index + i]) - dp[index + i])

                dp[index] = ans
            

        score = dp[0]

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"