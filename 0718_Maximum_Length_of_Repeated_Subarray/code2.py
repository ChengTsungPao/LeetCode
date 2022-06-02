class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)
        
        def condition(length):
            if length == 0:
                return True
            
            k = 0
            cache1 = set()
            for i in range(n):
                k = 101 * k + nums1[i]
                if i >= length - 1:
                    cache1.add(k)
                    k -= nums1[i - length + 1] * 101 ** (length - 1)
                    
            k = 0
            cache2 = set()
            for j in range(m):
                k = 101 * k + nums2[j]
                if j >= length - 1:
                    cache2.add(k)
                    k -= nums2[j - length + 1] * 101 ** (length - 1)
                    
            return len(cache1 & cache2) > 0
        
        
        left = 0
        right = min(n, m) + 1
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                left = mid + 1
            else:
                right = mid
                
        return left - 1