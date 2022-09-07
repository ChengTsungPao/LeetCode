class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        
        n = len(p)
        
        cache = set()
        for i in range(n):
            s = p[i]
            cache.add(s)
            for j in range(i + 1, n):
                if ord(p[j]) - ord(p[j - 1]) in {1, -25}:
                    s += p[j]
                    cache.add(s)
                else:
                    break

        return len(cache)