class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        
        n = len(s)
        
        cache = set()
        def recur(index):
            
            if index >= n:
                return 0

            ans = -float("inf")
            str_ = ""
            for i in range(index, n):
                str_ += s[i]

                if str_ not in cache:
                    cache.add(str_)
                    ans = max(ans, recur(i + 1) + 1)
                    cache.remove(str_)
                
            return ans
        
        return recur(0)