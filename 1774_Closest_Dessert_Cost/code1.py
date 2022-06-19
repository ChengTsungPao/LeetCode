class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:

        n = len(toppingCosts)
        toppingCosts.sort()
        maxBaseToppingCost = max(max(baseCosts), max(toppingCosts))
        
        def recur(index, target):
            if index >= n:
                return 0
            
            if target < -maxBaseToppingCost * 2:
                return -float("inf")
            
            cost = toppingCosts[index]
            target1 = recur(index + 1, target - cost * 0) + cost * 0
            target2 = recur(index + 1, target - cost * 1) + cost * 1
            target3 = recur(index + 1, target - cost * 2) + cost * 2
            ans = min((abs(target1 - target), target1), \
                      (abs(target2 - target), target2), \
                      (abs(target3 - target), target3) )
            
            return ans[1]
        
        ans = float("inf"), float("inf")
        for baseCost in baseCosts:
            targeti = recur(0, target - baseCost) + baseCost
            ans = min(ans, (abs(targeti - target), targeti))
        
        return ans[1]