class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ans = -float("inf")
        curMin = curSum = 0
        
        for num in nums:
            curSum += num
            ans = max(ans, curSum - curMin)
            curMin = min(curMin, curSum)
            
        return ans