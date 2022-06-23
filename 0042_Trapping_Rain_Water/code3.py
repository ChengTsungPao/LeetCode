class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        
        prefixMax = [0] * n
        suffixMax = [0] * n
        
        prefixMax[ 0] = height[ 0]
        suffixMax[-1] = height[-1]
        
        for i in range(1, n):
            prefixMax[ i] = max(prefixMax[ i - 1], height[ i])
            suffixMax[~i] = max(suffixMax[~i + 1], height[~i])

        ans = 0
        for i in range(1, n - 1):
            ans += max(min(prefixMax[i - 1], suffixMax[i + 1]) - height[i], 0)
                
        return ans