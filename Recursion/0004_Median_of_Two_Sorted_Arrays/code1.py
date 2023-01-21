class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def findkthSmallestNum(nums1, nums2, k):
            m, n = len(nums1), len(nums2)
            
            if k >= m + n:
                return -1
            
            if m > n:
                return findkthSmallestNum(nums2, nums1, k)
            
            if not nums1:
                return nums2[k]
            elif m + n - 1 == k:
                return max(nums1[-1], nums2[-1])
            
            i = min(m - 1, k // 2)
            j = min(n - 1, k - i)
            
            if nums1[i] > nums2[j]:
                return findkthSmallestNum(nums1[:i], nums2[j:], k - j)
            else:
                return findkthSmallestNum(nums1[i:], nums2[:j], k - i)
            
        length = len(nums1) + len(nums2)
        
        if length % 2:
            return findkthSmallestNum(nums1, nums2, length // 2)
        else:
            return (findkthSmallestNum(nums1, nums2, length // 2 - 1) + findkthSmallestNum(nums1, nums2, length // 2)) / 2
        