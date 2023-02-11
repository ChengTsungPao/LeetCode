class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        n = len(customers)
        
        totalScore = maxWindowScore = windowScore = 0
        for i in range(n):
            totalScore += customers[i] * (not grumpy[i])
            windowScore += customers[i] * grumpy[i]
            maxWindowScore = max(maxWindowScore, windowScore)

            if i + 1 >= minutes:
                windowScore -= customers[i - minutes + 1] * grumpy[i - minutes + 1]
            
        return totalScore + maxWindowScore