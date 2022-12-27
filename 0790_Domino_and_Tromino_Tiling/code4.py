class Solution:
    def numTilings(self, n: int) -> int:
        
        MOD = pow(10, 9) + 7
        
        @functools.lru_cache(None)
        def recur(i, j):
            if i >= n or j >= n:
                return (i == n and j == n) * 1
            
            if i > j:
                return recur(i, j + 2) + recur(i + 1, j + 2)
            elif i == j:
                return recur(i + 1, j + 1) + recur(i + 2, j + 1) + recur(i + 1, j + 2) + recur(i + 2, j + 2)
            else:
                return recur(i + 2, j) + recur(i + 2, j + 1)
            
        return recur(0, 0) % MOD
