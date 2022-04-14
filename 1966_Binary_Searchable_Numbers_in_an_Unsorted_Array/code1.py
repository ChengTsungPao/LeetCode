class Solution:
    def binarySearchableNumbers(self, nums: List[int]) -> int:
        
        # 當"前面的所有數字都比當前數字小"且"後面的所有數字比當前數字大"，代表可以搜尋到
        
        n = len(nums)
        
        prefixMax = [0] * n
        prefixMax[0] = nums[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], nums[i])
            
        suffixMin = [0] * n
        suffixMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i + 1], nums[i])
            
        ans = 0
        for i in range(n):
            if nums[i] == prefixMax[i] and nums[i] == suffixMin[i]:
                ans += 1
                
        return ans