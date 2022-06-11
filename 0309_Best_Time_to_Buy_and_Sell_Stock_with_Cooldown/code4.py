class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        maxScore = {}
        def getMaxScore(index):
            
            if index not in maxScore:
                
                if index >= n - 1:
                    return 0

                maxScore[index] = max(getMaxScore(index + 1), prices[index + 1] + recur(index + 3))
                
            return maxScore[index]
        
        memo = {}
        def recur(index):
            
            if index not in memo:
                
                if index >= n - 1:
                    return 0
                
                memo[index] = max(recur(index + 1), getMaxScore(index) - prices[index])
                
            return memo[index]
        
        return recur(0)