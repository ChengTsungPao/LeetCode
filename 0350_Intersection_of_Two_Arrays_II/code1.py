class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1 = collections.Counter(nums1)
        nums2 = collections.Counter(nums2)
        for n in nums1 & nums2:
            ans += [n] * min(nums1[n], nums2[n])
        return ans