class Solution:
    def jump(self, nums: List[int]) -> int:
        
        ans, farjumps, cur_jump_end = 0, 0, 0
        
        for i in range(len(nums) - 1):
            
            farjumps = max(farjumps, nums[i] + i)
            
            if i == cur_jump_end:
                cur_jump_end = farjumps
                ans += 1
                
        return ans