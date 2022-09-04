class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        ans = 1
        dp_p = [1] * n
        dp_n = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp_p[i] = max(dp_p[i], dp_n[j] + 1)
                elif nums[i] < nums[j]:
                    dp_n[i] = max(dp_n[i], dp_p[j] + 1)
                    
            ans = max(ans, dp_p[i], dp_n[i])
                    
        return ans