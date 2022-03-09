class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        
        gas *= 2
        cost *= 2
        
        i = 0
        j = 0
        curGas = 0
        
        while i < n and j < n * 2:
            curGas += gas[j] - cost[j]

            while curGas < 0 and i < j + 1:
                curGas += cost[i] - gas[i]
                i += 1
                
            if j - i + 1 >= n:
                return i
            
            j += 1
            
        return -1