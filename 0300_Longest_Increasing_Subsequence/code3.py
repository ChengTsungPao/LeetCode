class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        ans, dp, count = 1, [nums[-1]], [1]
        
        for i in range(len(nums) - 2, -1, -1):
            
            index = bisect.bisect_right(dp, nums[i])
            
            dp.insert(index, nums[i])
            count.insert(index, max(count[index:], default = 0) + 1)
                
            ans = max(ans, count[index])
            
        return ans