class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        nums.append(float("inf"))
        n = len(nums)
        
        for i in range(1, n):
            missCount = nums[i] - nums[i - 1] - 1
            if k > missCount:
                k -= missCount
            else:
                return nums[i - 1] + k
            
        return -1