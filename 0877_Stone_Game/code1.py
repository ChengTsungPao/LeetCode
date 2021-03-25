class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(i, j, Alex, Lee, who):
            if (i, j) not in dp:
                if i > j:
                    return Alex, Lee
                if who:
                    Alextmp1, Leetmp1 = dfs(i + 1, j - 0, Alex + piles[i], Lee, not who)
                    Alextmp2, Leetmp2 = dfs(i + 0, j - 1, Alex + piles[j], Lee, not who)
                    if Alextmp1 - Alex > Alextmp2 - Alex:
                        dp[i, j] = Alextmp1 - Alex, Leetmp1 - Lee
                    else:
                        dp[i, j] = Alextmp2 - Alex, Leetmp2 - Lee
                else:
                    Alextmp1, Leetmp1 = dfs(i + 1, j - 0, Alex, Lee + piles[i], not who)
                    Alextmp2, Leetmp2 = dfs(i + 0, j - 1, Alex, Lee + piles[j], not who)
                    if Leetmp1 - Lee > Leetmp2 - Lee:
                        dp[i, j] = Alextmp1 - Alex, Leetmp1 - Lee
                    else:
                        dp[i, j] = Alextmp2 - Alex, Leetmp2 - Lee
            return Alex + dp[i, j][0], Lee + dp[i, j][1]

        Alex, Lee = dfs(0, len(piles) - 1, 0, 0, True)
        if Alex > Lee:
            return True
        else:
            return False