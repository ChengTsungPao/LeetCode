class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        n = len(nums)
        
        ans = []
        count = 1
        
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                if n // 3 < count:
                    ans.append(nums[i - 1])
                count = 1
        
        if n // 3 < count:
            ans.append(nums[-1])
            
        return ans