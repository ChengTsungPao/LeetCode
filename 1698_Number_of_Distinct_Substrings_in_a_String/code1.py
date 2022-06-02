class Solution:
    def countDistinct(self, s: str) -> int:
        
        n = len(s)
        cache = set()
        
        def getSubString(length, cacheValue):            
            k = 0
            for i in range(n):
                k = 27 * k + ord(s[i]) - 96
                if i >= length - 1:
                    cache.add(k)
                    k -= (ord(s[i - length + 1]) - 96) * cacheValue
        
        cacheValue = 1
        for length in range(1, n + 1):
            getSubString(length, cacheValue)
            cacheValue *= 27
            
        return len(cache)