class Solution:
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)
    
    
    def twoSum(self, nums, target):
        ans = set()
        visited = set()
        for num in nums:
            if target - num in visited:
                ans.add((num, target - num))
            visited.add(num)
        return ans
    
    
    def kSum(self, nums, target, k):
        if not nums or target < nums[0] * k or target > nums[-1] * k:
            return []
        
        if k == 2:
            return self.twoSum(nums, target)
        
        ans = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
                
            for ret in self.kSum(nums[i + 1:], target - nums[i], k - 1):
                ans.append([nums[i]] + list(ret))
                
        return ans