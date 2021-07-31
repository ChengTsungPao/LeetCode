class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_peak(nums):
            left, right = 0, len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < nums[left]:
                    right = mid
                elif nums[mid] < nums[mid + 1]:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        peakIndex = find_peak(nums)

        if nums[0] > target:
            index = bisect.bisect_left(nums, target, peakIndex + 1, len(nums))
        else:    
            index = bisect.bisect_left(nums, target, 0, peakIndex + 1)

        return index if index < len(nums) and nums[index] == target else -1               
     