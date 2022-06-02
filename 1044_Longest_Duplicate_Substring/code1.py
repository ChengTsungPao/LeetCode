class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        n = len(s)
        
        cacheValue = [1] * n
        for i in range(1, n):
            cacheValue[i] = 26 * cacheValue[i - 1]
        
        def condition(length):
            if length == 0:
                return True, ""
            
            k = 0
            cache = set()
            for i in range(n):
                k = 26 * k + ord(s[i]) - 97
                if k in cache:
                    return True, s[i - length + 1: i + 1]
                if i >= length - 1:
                    cache.add(k)
                    k -= (ord(s[i - length + 1]) - 97) * cacheValue[length - 1]
                    
            return False, ""
        
        ans = ""
        left = 0
        right = n
        while left < right:
            mid = left + (right - left) // 2
            isValid, subStr = condition(mid)
            if isValid:
                ans = subStr
                left = mid + 1
            else:
                right = mid
                
        return ans