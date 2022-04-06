class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        M = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        
        ans = 0
        i, j = 0, n - 1
        while i <= j:
            if nums[i] + nums[j] <= target:
                ans += 2 ** (j - i)
                i += 1
            else:
                j -= 1
                
        return ans % M