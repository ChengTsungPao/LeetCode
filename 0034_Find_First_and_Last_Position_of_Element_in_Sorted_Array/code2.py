class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bisect_left(nums, target):
            ans = -1
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    ans = mid
                    right = mid - 1
            return ans
        
        def bisect_right(nums, target):
            ans = -1
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    ans = mid
                    left = mid + 1
            return ans
        
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        
        return [left, right]