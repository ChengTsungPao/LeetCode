class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def findkthSmallestNum(nums1, nums2, k):
            if k >= len(nums1) + len(nums2):
                return -1

            if len(nums1) > len(nums2):
                return findkthSmallestNum(nums2, nums1, k)

            if not nums1:
                return nums2[k]
            elif len(nums1) + len(nums2) - 1 == k:
                return max(nums1[-1], nums2[-1])

            i = min(len(nums1) - 1, k // 2)
            j = min(len(nums2) - 1, k - i)

            if nums1[i] > nums2[j]:
                return findkthSmallestNum(nums1[:i], nums2[j:], k - j)
            else:
                return findkthSmallestNum(nums1[i:], nums2[:j], k - i)
        
        
        m = len(nums1)
        n = len(nums2)
        
        length = m + n
        
        if length % 2 == 1:
            return findkthSmallestNum(nums1, nums2, length // 2)
        else:
            return (findkthSmallestNum(nums1, nums2, length // 2 - 1) + findkthSmallestNum(nums1, nums2, length // 2)) / 2 