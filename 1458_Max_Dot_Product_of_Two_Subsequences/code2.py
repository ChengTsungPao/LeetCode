class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)

        @functools.lru_cache(None)
        def recur(i, j):
            if i >= n or j >= m:
                return 0
            return max(nums1[i] * nums2[j] + recur(i + 1, j + 1), recur(i + 1, j), recur(i, j + 1))
        
        ans = recur(0, 0)
        # 若出現負值代表nums1全正和nums2全負，或者相反
        return ans if ans > 0 else min(nums1, key = abs) * min(nums2, key = abs)