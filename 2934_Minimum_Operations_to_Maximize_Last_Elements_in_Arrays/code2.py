class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        dp1 = dp2 = 0
        for num1, num2 in zip(nums1, nums2):
            if max(nums1[-1], nums2[-1]) < max(num1, num2): return -1
            if min(nums1[-1], nums2[-1]) < min(num1, num2): return -1
            if num1 > nums1[-1] or num2 > nums2[-1]: dp1 += 1
            if num1 > nums2[-1] or num2 > nums1[-1]: dp2 += 1
        
        return min(dp1, dp2)