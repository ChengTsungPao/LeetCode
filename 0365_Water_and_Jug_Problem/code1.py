class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        
        total = jug1Capacity + jug2Capacity
        
        def getNextState(capacity):
            nextState = [
                abs(total - capacity), 
                abs(jug1Capacity - capacity),
                abs(jug2Capacity - capacity),
                abs(jug1Capacity + capacity),
                abs(jug2Capacity + capacity),
            ]
            return nextState
            
        
        dp = [False] * (total + 1)
        dp[jug1Capacity] = True
        dp[jug2Capacity] = True
        dp[total] = True
        
        que = collections.deque([jug1Capacity, jug2Capacity, total])
        
        while que:
            capacity = que.pop()
            
            if capacity == targetCapacity:
                return True
            
            for nextCapacity in getNextState(capacity):
                if not (0 <= nextCapacity <= total):
                    continue
                
                if not dp[nextCapacity]:
                    dp[nextCapacity] = True
                    que.appendleft(nextCapacity)
                    
        return False
