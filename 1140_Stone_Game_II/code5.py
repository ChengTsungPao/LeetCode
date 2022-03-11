class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        # 計算 Alice - Bob 和 Alice + Bob，解出 Alice
        
        '''
        Recursion
            index => 0 ~ n
            M     => 1 ~ n
        '''
        
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for index in range(n, -1, -1):
            for M in range(n, 0, -1):
                if index >= n:
                    dp[index][M] = 0
                else:
                    ans = -float("inf")
                    for x in range(1, 2 * M + 1):
                        if index + x >= n:
                            ans = max(ans, sum(piles[index: index + x]) - 0)
                        else:
                            ans = max(ans, sum(piles[index: index + x]) - dp[index + x][max(x, M)])

                    dp[index][M] = ans        
                    
        add = sum(piles)
        sub = dp[0][1]
        
        return (add + sub) // 2