class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        M = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        
        ans = 0
        for i in range(n):
            if target - nums[i] >= nums[i]:
                j = bisect.bisect_right(nums, target - nums[i], i, n)
                ans += 2 ** (j - i - 1)
                
        return ans % M