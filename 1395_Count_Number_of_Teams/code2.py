class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        
        dp1 = [[1] + [0] * 2 for _ in range(n)]
        dp2 = [[1] + [0] * 2 for _ in range(n)]
        
        ans = 0
        for i in range(1, n):
            for j in range(i):
                if rating[j] < rating[i]:
                    dp1[i][1] += dp1[j][0]
                    dp1[i][2] += dp1[j][1]
                    
                if rating[j] > rating[i]:
                    dp2[i][1] += dp2[j][0]
                    dp2[i][2] += dp2[j][1]
                    
            ans += dp1[i][2] + dp2[i][2]
        
        return ans