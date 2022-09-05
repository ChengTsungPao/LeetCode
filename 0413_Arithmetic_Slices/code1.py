class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        ans = 0
        diff = length = 1
        
        for i in range(1, n):
            if length == 1 or diff == nums[i] - nums[i - 1]:
                length += 1
            else:
                ans += (length - 2) * (length - 1) // 2 if length >= 3 else 0
                length = 2
                
            diff = nums[i] - nums[i - 1]
                
        ans += (length - 2) * (length - 1) // 2 if length >= 3 else 0
        
        return ans