class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            if a % b == 0:
                return b
            return gcd(a % b, b)
                
        n = len(nums)
        
        ans = 0
        times = factorial(n)
        
        while times > 0:
            j = n - 2
            while j >= 0 and nums[j] >= nums[j + 1]:
                j -= 1
            
            if j < 0:
                nums[:] = reversed(nums)
            else:
                nums[j + 1:] = reversed(nums[j + 1:])
                k = bisect.bisect_right(nums, nums[j], j + 1, n)
                nums[j], nums[k] = nums[k], nums[j]
                
            times -= 1
            ans = max(ans, sum([(i // 2 + 1) * gcd(nums[i], nums[i + 1]) for i in range(0, n, 2)]))

        return ans