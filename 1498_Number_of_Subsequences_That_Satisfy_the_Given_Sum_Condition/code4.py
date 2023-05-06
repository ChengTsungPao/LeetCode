class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        MOD = pow(10, 9) + 7
        
        n = len(nums)
        nums.sort()
        
        ans = 0
        i, j = 0, n - 1
        while i <= j:
            if nums[i] + nums[j] <= target:
                m = j - i - 1
                ans += (pow(2, m + 1, MOD) - 1) + 1
                i += 1
            else:
                j -= 1
                
        return ans % MOD