class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        
        curGas = 0
        i = j = 0
        
        while i < n:
            
            while j < n * 2:
                curGas += gas[j % n] - cost[j % n]
                j += 1
                if curGas < 0:
                    break
                elif j - i >= n:
                    return i
                
            while i < j and i < n and curGas < 0:
                curGas -= gas[i] - cost[i]
                i += 1
                
        return -1
        