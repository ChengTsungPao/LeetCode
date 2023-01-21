class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = -float("inf")
        curSum = 0
        
        for num in nums:
            curSum += num
            ans = max(ans, curSum)
            
            if curSum < 0:
                curSum = 0
            
        return ans