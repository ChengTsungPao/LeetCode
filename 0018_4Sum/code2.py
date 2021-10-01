class Solution:
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.kSum(sorted(nums), target, 4)
        
    def kSum(self, nums, target, k):
        
        if nums == [] or nums[0] * k > target or target > nums[-1] * k:
            return []
        
        if k == 2:
            return self.twoSum(nums, target)
        
        ans = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            for ret in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                ans.append([nums[i]] + ret)
                
        return ans
        
    def twoSum(self, nums, target):
        ret = []
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                ret.append([nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left - 1] == nums[left]:
                    left += 1
            
        return ret
