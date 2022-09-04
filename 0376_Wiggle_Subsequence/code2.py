class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        ans = 1
        dp_p = [1] * n
        dp_n = [1] * n
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp_p[i] = max(dp_p[i], dp_n[i - 1] + 1)
                dp_n[i] = dp_n[i - 1]
            elif nums[i] < nums[i - 1]:
                dp_n[i] = max(dp_n[i], dp_p[i - 1] + 1)
                dp_p[i] = dp_p[i - 1]
            else:
                dp_p[i] = dp_p[i - 1]
                dp_n[i] = dp_n[i - 1]
                    
            ans = max(ans, dp_p[i], dp_n[i])
                    
        return ans