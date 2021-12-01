class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        '''
        dp[i][target] = 前i個cost總合為target的最大組合
        
        Init:
            cost = cost總合
            score = cost總合為target的最大組合
        
            dp[0][target] = "
            dp[i][0] = ""
        
        Method:
            dp[i][target] = max(dp[i - 1][target], biggestNum(dp[i][target - cost[i]] + str(i + 1)))
        '''
        
        def biggestNum(num):
            return "".join(sorted(list(num), reverse = True))
        
        def maxNum(num1, num2):
            if len(num1) > len(num2):
                return num1
            elif len(num1) < len(num2):
                return num2
            else:
                return max(num1, num2)
        
        dp = [[""] * (target + 1) for _ in range(len(cost) + 1)]       
        
        for i in range(1, len(cost) + 1):
            for target_ in range(1, target + 1):
                if target_ - cost[i - 1] == 0 or (target_ - cost[i - 1] > 0 and dp[i][target_ - cost[i - 1]] != ""):
                    dp[i][target_] = maxNum(dp[i - 1][target_], biggestNum(dp[i][target_ - cost[i - 1]] + str(i)))
                else:
                    dp[i][target_] = dp[i - 1][target_]
           
        return dp[-1][-1] if dp[-1][-1] != "" else "0"
    