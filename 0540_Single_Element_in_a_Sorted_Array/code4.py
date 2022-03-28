class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if mid + 1 < n and nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            elif mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                if (mid - 1) % 2 == 0:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            else:
                return nums[mid]
            
        return -1