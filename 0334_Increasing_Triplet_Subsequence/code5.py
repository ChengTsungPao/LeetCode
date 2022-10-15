class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        prefixMin = [nums[ 0]] * n
        suffixMax = [nums[-1]] * n
        for i in range(1, n):
            prefixMin[ i] = min(prefixMin[ i - 1], nums[ i])
            suffixMax[~i] = max(suffixMax[~i + 1], nums[~i])
            
        for i in range(1, n - 1):
            if prefixMin[i - 1] < nums[i] < suffixMax[i + 1]:
                return True
            
        return False