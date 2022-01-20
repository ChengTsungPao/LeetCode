class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                index = bisect.bisect_left(nums, target - (nums[i] + nums[j]), j + 1, len(nums))
                ans += (index - 1) - j
                
        return ans