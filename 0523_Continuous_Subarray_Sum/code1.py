class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # preSum
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        
        # (preSum[j] - preSum[i]) % k = 0 => preSum[i] % k = preSum[j] % k
        cache = set()
        for j in range(1, n + 1):
            if preSum[j] % k in cache:
                return True
            cache.add(preSum[j - 1] % k)
            
        return False