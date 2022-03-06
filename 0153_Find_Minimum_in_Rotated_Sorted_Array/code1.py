class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def find_peak(nums):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < nums[left]:
                    right = mid
                elif nums[mid] < nums[mid + 1]:
                    left = mid + 1
                else:
                    return mid
            return left
        
        index = find_peak(nums)
        
        return nums[index + 1] if index < len(nums) - 1 else nums[0]