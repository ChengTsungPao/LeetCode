class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        sum_ = gasSum = costSum = 0
        index = 0

        for i in range(len(gas)):
            if sum_ < 0:
                sum_ = 0
                index = i
                
            gasSum += gas[i]
            costSum += cost[i]
            sum_ += gas[i] - cost[i]
            
        return index if gasSum >= costSum else -1