class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        '''
        1 => cost[0] * abs(nums[0] - 1) + cost[1] * abs(nums[1] - 1) + cost[2] * abs(nums[2] - 1) + cost[3] * abs(nums[3] - 1)
             cost[0] * (nums[0] - 1) + cost[1] * (nums[1] - 1) + cost[2] * (nums[2] - 1) + cost[3] * (nums[3] - 1) 
            total1
            
        2 => cost[0] * abs(nums[0] - 2) + cost[1] * abs(nums[1] - 2) + cost[2] * abs(nums[2] - 2) + cost[3] * abs(nums[3] - 2)
             cost[0] * abs(nums[0] - 2) + cost[1] * (nums[1] - 2) + cost[2] * (nums[2] - 2) + cost[3] * (nums[3] - 2)
        
            total1 -= -cost[0] + cost[1] + cost[2] + cost[3]
            total2
            
        3 => 
            total2 -= -cost[0] - cost[1] + cost[2] + cost[3]
            total3
        4 => 
            total3 -= -cost[0] - cost[1] - cost[2] + cost[3]
        '''
        
        arr = sorted(zip(nums, cost))
        _min, _max = arr[0][0], arr[-1][0]
        
        n = len(arr)
        preSum = [arr[0][1]] * n
        for i in range(1, n):
            preSum[i] = preSum[i - 1] + arr[i][1]
            
        suffixSum = [arr[-1][1]] * n
        for i in range(n - 2, -1, -1):
            suffixSum[i] = suffixSum[i + 1] + arr[i][1]
            
        total = sum([_cost * (_num - _min) for _num, _cost in arr])
        ans = total
        for val in range(_min + 1, _max + 1):
            index = bisect.bisect_right(arr, (val, -1))
            total -= -preSum[index - 1] + suffixSum[index]
            ans = min(ans, total)
            
        return ans