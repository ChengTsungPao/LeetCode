class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        cache = set()
        ans = _sum = i = 0
        for j in range(n):
            while nums[j] in cache:
                cache.remove(nums[i])
                _sum -= nums[i]
                i += 1
            
            cache.add(nums[j])
            _sum += nums[j]
            if j - i + 1 == k:
                ans = max(ans, _sum)
                cache.remove(nums[i])
                _sum -= nums[i]
                i += 1
                
        return ans