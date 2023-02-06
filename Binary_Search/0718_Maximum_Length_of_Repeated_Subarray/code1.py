class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        def getSubarraySet(nums, length):
            key = 0
            powValue = pow(101, length - 1)
            subarray_set = set()
            for i, num in enumerate(nums):
                key = 101 * key + num
                if i + 1 >= length:
                    subarray_set.add(key)
                    key -= powValue * nums[i - length + 1]
            return subarray_set
        
        def getCondition(nums1, nums2, length):
            nums1_subarray_set = getSubarraySet(nums1, length)
            nums2_subarray_set = getSubarraySet(nums2, length)
            return len(nums1_subarray_set & nums2_subarray_set) >= 1
        
        m = len(nums1)
        n = len(nums2)
        
        ans = 0
        left, right = 1, min(m, n) + 1
        while left <= right:
            mid = left + (right - left) // 2
            if getCondition(nums1, nums2, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return ans