class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        # Loop1: 若出現 nums[i] <= nums[j] (i < j), 此時忽略nums[j]因為跟nums[i]比較即可
        # Loop2: 若大於當前stack[-1]，代表之前被pop掉的num都大於        
        
        n = len(nums)
        
        stack = []
        for i in range(n):
            if not stack or stack[-1][0] > nums[i]:
                stack.append((nums[i], i))
        
        ans = 0
        for j in range(n - 1, -1, -1):
            while stack and stack[-1][0] <= nums[j]:
                num, i = stack.pop()
                ans = max(ans, j - i)
                
        return ans