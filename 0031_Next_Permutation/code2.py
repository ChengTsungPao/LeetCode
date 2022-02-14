class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        def binarySearch(target, left, right):
            ans = -1
            
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] > target:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return ans
            
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        
        if i - 1 >= 0:
            index = binarySearch(nums[i - 1], i, len(nums) - 1)
            nums[i - 1], nums[index] = nums[index], nums[i - 1]
            nums[i:] = reversed(nums[i:])
        else:
            nums.reverse()