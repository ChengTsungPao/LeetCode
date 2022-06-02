class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        def getCache(length, nums):
            k = 0
            cache = set()
            for i in range(len(nums)):
                k = 101 * k + nums[i]
                if i >= length - 1:
                    cache.add(k)
                    k -= nums[i - length + 1] * 101 ** (length - 1)
            return cache
        
        def condition(length):
            if length == 0:
                return True
            
            cache1 = getCache(length, nums1)
            cache2 = getCache(length, nums2)                    
            return len(cache1 & cache2) > 0
        
        
        m = len(nums1)
        n = len(nums2)
        
        left = 0
        right = min(m, n) + 1
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                left = mid + 1
            else:
                right = mid
                
        return left - 1