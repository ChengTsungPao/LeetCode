class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        def myPow(x, n, M):
            if n == 0:
                return 1
            
            ans = x
            times = 1
            while times * 2 < n:
                ans *= ans
                ans %= M
                times *= 2

            return ans * myPow(x, n - times, M)
        
        
        M = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        
        ans = 0
        i, j = 0, n - 1
        while i <= j:
            if nums[i] + nums[j] <= target:
                ans += myPow(2, (j - i), M)
                i += 1
            else:
                j -= 1
                
        return ans % M