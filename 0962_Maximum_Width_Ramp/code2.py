class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        prefixMin = [ float("inf")] * n
        prefixMin[ 0] = nums[ 0]
        
        suffixMax = [-float("inf")] * n
        suffixMax[-1] = nums[-1]
        
        for i in range(1, n):
            prefixMin[ i] = min(prefixMin[ i - 1], nums[ i])
            suffixMax[~i] = max(suffixMax[~i + 1], nums[~i])
        
        ans = 0
        index = 0
        length = 1
        
        while index + length < n:
            if prefixMin[index] <= suffixMax[index + length]:
                ans = length
                length += 1
            else:
                index += 1
            
        return ans