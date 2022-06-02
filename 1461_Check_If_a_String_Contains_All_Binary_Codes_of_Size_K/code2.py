class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        n = len(s)
        
        key = 0
        cache = set()
        powK = 2 ** (k - 1)
        
        for i in range(n):
            key = 2 * key + int(s[i])
            if i >= k - 1:
                cache.add(key)
                key -= int(s[i - k + 1]) * powK
   
        return len(cache) == powK * 2