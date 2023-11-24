class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        def getMinOpr(nums1, nums2):
            countOpr = 0
            for i in range(n - 1):
                if nums1[i] > nums1[-1] or nums2[i] > nums2[-1]:
                    if not (nums2[i] <= nums1[-1] and nums1[i] <= nums2[-1]):
                        return float("inf")
                    countOpr += 1
            return countOpr
        
        ans1 = getMinOpr(nums1, nums2)
        nums1[-1], nums2[-1] = nums2[-1], nums1[-1]
        ans2 = getMinOpr(nums1, nums2) + 1
        
        ans = min(ans1, ans2)
        return ans if ans != float("inf") else -1 