class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        memo = {}
        def recur(i, j, who):
            
            if (i, j) not in memo:
                
                if i > j:
                    return 0
                
                if who:
                    ans = max(recur(i + 1, j, not who) + nums[i], recur(i, j - 1, not who) + nums[j])
                else:
                    ans = min(recur(i + 1, j, not who) - nums[i], recur(i, j - 1, not who) - nums[j])
                    
                memo[i, j] = ans
                
            return memo[i, j]
        
        return recur(0, len(nums) - 1, True) >= 0 