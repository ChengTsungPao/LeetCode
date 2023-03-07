class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        
        if len(nums) == 3:
            return 0
        
        # 其實找前三大或前三小就好
        nums.sort()
        return min(nums[-2] - nums[1], nums[-1] - nums[2], nums[-3] - nums[0])