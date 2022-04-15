class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ans = []
        
        while not ans or ans[0] != nums:
            ans.append(nums.copy())
            
            i = n - 1
            while i - 1 >= 0 and nums[i - 1] > nums[i]:
                i -= 1
            i -= 1
            
            if i < 0:
                nums.reverse()
                continue
            
            j = n - 1
            while j - 1 >= 0 and nums[i] >= nums[j]:
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1:] = reversed(nums[i + 1:])

        return ans