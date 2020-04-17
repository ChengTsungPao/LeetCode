class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from scipy.special import comb
        return comb(m+n-2,n-1,exact=True)