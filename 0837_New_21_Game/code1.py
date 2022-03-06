class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        '''
        方法:
            1. 利用前面maxPts個數字來計算獲得當前分數的機率
            2. 計算所有可能的分數再一步，其分數可能超過n的機率
        範例:
            n = 21, k = 17, maxPts = 10
            score = 12 => +10     > 21
                    13 => +9 ~ 10 > 21
                    14 => +8 ~ 10 > 21
                    15 => +7 ~ 10 > 21
                    16 => +6 ~ 10 > 21
        '''
        # 排除邊界條件
        if k == 0:
            return 1.0
        elif n == 0:
            return 0.0

        # 計算獲得該分數的機率
        prob = 1 / maxPts
        dp = [1] * k

        prob_sum = 1
        i, j = 0, 1
        while j < k:
            dp[j] = prob_sum * prob

            prob_sum += dp[j]
            j += 1
            
            if j - i > maxPts:
                prob_sum -= dp[i]
                i += 1
        
        # 計算超過n的機率
        overProb = 0
        for totalScore in range(max(n - maxPts + 1, 1), k):
            overProb += dp[totalScore] * (maxPts - (n - totalScore)) * prob

        ans = 1 - overProb
        if n < maxPts:
            ans -= (maxPts - n) * prob

        return ans