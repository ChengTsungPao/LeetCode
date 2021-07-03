class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        length = len(rating)
        
        dp = []
        for i in range(length):
            dp.append([0, 0])
            for j in range(i + 1, length):
                if rating[i] > rating[j]:
                    dp[i][0] += 1
                else:
                    dp[i][1] += 1
        
        ans = 0
        for i in range(length):
            for j in range(i + 1, length):
                if rating[i] > rating[j]:
                    ans += dp[j][0]
                else:
                    ans += dp[j][1]
                    
        return ans
