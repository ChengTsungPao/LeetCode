class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        
        # step1 dp[i][j] = dp[i - 1][j]，先確認是否能從位置(i - 1, j)過來 => 最快跳到
        # step2 dp[i][j] = float("inf")，接著把有石頭的位置數值設成無限大  => 不可能跳到
        # step3 dp[i][j] = min(dp[i][j], 青蛙側邊跳法1, 青蛙側邊跳法2)    => 側邊跳的方法 (有石頭不更新)
        
        dp = [[1, 0, 1]]
        
        for i in range(1, len(obstacles)):
            
            dp.append([dp[i - 1][0], dp[i - 1][1], dp[i - 1][2]])
            
            if obstacles[i] != 0:
                dp[-1][obstacles[i] - 1] = float("inf")
            
            dp[-1][0] = float("inf") if obstacles[i] == 1 else min(dp[-1][0], dp[i][1] + 1, dp[i][2] + 1)
            dp[-1][1] = float("inf") if obstacles[i] == 2 else min(dp[-1][1], dp[i][0] + 1, dp[i][2] + 1)
            dp[-1][2] = float("inf") if obstacles[i] == 3 else min(dp[-1][2], dp[i][0] + 1, dp[i][1] + 1)
     
        return min(dp[-1])
