class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp_p = 1
        dp_n = 1
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp_p = max(dp_p, dp_n + 1)
            elif nums[i] < nums[i - 1]:
                dp_n = max(dp_n, dp_p + 1)

        return max(dp_p, dp_n)