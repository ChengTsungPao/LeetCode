class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)
        
        if m > n:
            return self.maxDotProduct(nums2, nums1)

        @functools.lru_cache(None)
        def recur(i, j):
            if i >= n or j >= m:
                return 0
            
            ans = recur(i + 1, j)
            for k in range(j, m):
                if nums1[i] * nums2[k] >= 0:
                    ans = max(ans, nums1[i] * nums2[k] + recur(i + 1, k + 1))
                
            return ans
        
        ans = recur(0, 0)
        # 若出現負值代表nums1全正和nums2全負，或者相反
        return ans if ans > 0 else min(nums1, key = abs) * min(nums2, key = abs)