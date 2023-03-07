class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        
        ans = 0
        visited = set()
        for i in range(n + 1):
            if preSum[i] - target in visited:
                ans += 1
                visited = set()
                
            visited.add(preSum[i])
            
        return ans