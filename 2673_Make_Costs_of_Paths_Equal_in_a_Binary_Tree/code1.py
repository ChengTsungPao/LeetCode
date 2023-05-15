class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        
        cost = [0] + cost
        
        @functools.lru_cache(None)
        def getMaxCost(index):
            if index >= n + 1:
                return 0
            return cost[index] + max(getMaxCost(index * 2), getMaxCost(index * 2 + 1))
        
        def recur(index, remainder_cost):
            if index >= n + 1:
                return 0
            increment = remainder_cost - getMaxCost(index)
            return increment + recur(index * 2, remainder_cost - (increment + cost[index])) + recur(index * 2 + 1, remainder_cost - (increment + cost[index]))
        
        maxCost = getMaxCost(1)
        return recur(1, maxCost)