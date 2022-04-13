class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # 紀錄當前我能走到的最遠位置 (maxIndex)
        
        n = len(nums)
        
        maxIndex = 0
        for index in range(n):
            if index > maxIndex:
                return False
            maxIndex = max(maxIndex, index + nums[index])
            
        return True