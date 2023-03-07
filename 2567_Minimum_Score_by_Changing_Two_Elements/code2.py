class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        
        if len(nums) == 3:
            return 0
        
        min1 = min2 = min3 = float("inf")
        max1 = max2 = max3 = -float("inf")
        
        for num in nums:
            min3 = min(min3, num)
            max3 = max(max3, num)
            
            max1, max2, max3 = sorted([max1, max2, max3], reverse = True)
            min1, min2, min3 = sorted([min1, min2, min3])
        
        return min(max2 - min2, max1 - min3, max3 - min1)