class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        
        '''
        h(i, j) = |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j| = f(i) + g(j)
        
        f(i) = +arr1[i] + arr2[i] + i  <=>  g(j) = -arr1[j] - arr2[j] - j  <---  k = 0
        f(i) = +arr1[i] + arr2[i] - i  <=>  g(j) = -arr1[j] - arr2[j] + j  <---  k = 1
        f(i) = +arr1[i] - arr2[i] + i  <=>  g(j) = -arr1[j] + arr2[j] - j  <---  k = 2
        f(i) = +arr1[i] - arr2[i] - i  <=>  g(j) = -arr1[j] + arr2[j] + j  <---  k = 3
        f(i) = -arr1[i] + arr2[i] + i  <=>  g(j) = +arr1[j] - arr2[j] - j  <---  k = 4
        f(i) = -arr1[i] + arr2[i] - i  <=>  g(j) = +arr1[j] - arr2[j] + j  <---  k = 5
        f(i) = -arr1[i] - arr2[i] + i  <=>  g(j) = +arr1[j] + arr2[j] - j  <---  k = 6
        f(i) = -arr1[i] - arr2[i] - i  <=>  g(j) = +arr1[j] + arr2[j] + j  <---  k = 7
        '''
        
        # 計算所有可能正負號
        c = []
        for c1 in [1, -1]:
            for c2 in [1, -1]:
                for c3 in [1, -1]:
                    c.append((c1, c2, c3))
                    
        n = len(arr1)
        m = len(c)
        
        # 計算所有的f(i)
        f = [-float("inf")] * m
        for k, (c1, c2, c3) in enumerate(c):
            for i in range(n):
                f[k] = max(f[k], c1 * arr1[i] + c2 * arr2[i] + c3 * i)
                
        # 計算所有的g(j)        
        g = [-float("inf")] * m
        for k, (c1, c2, c3) in enumerate(c):
            for j in range(n):
                g[k] = max(g[k], -c1 * arr1[j] - c2 * arr2[j] - c3 * j)

        # 計算f(i)+g(j)最大值
        ans = 0
        for k in range(m):
            ans = max(ans, f[k] + g[k])
                
        return ans 