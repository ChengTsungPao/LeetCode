class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        numCosts = sorted(zip(nums, cost))
        
        index, count = 0, sum(cost) // 2
        while count >= 0:
            count -= numCosts[index][1]
            index += count >= 0
        val = numCosts[index][0]
        
        return sum([abs(_num - val) * _cost for _num, _cost in numCosts])