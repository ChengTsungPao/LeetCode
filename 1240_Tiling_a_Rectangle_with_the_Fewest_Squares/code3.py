class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n < m:
            n, m = m, n
        
        height = [0] * m
        
        def getMaxValidSize(start):
            end = start
            while end < m and height[start] == height[end]:
                end += 1
            return min(n - height[start], end - start)
        
        def setHeight(start, size, addHeight):
            for j in range(start, start + size):
                height[j] += addHeight
                
        def convertPos(i, j):
            if j >= m:
                i += 1
                j = 0
            while height[j] >= i + 1:
                j += 1
                if j >= m:
                    i += 1
                    j = 0
            return i, j
        
        memo = {str([n] * (m - size) + [n - size] * size) : 1 for size in range(1, min(n, m) + 1)}
        
        minStep = float("inf")
        def recur(i, j, step):
            nonlocal minStep
            
            if step >= minStep:
                return float("inf")
            
            key = str(height)
            
            if key not in memo:
            
                i, j = convertPos(i, j)

                if i >= n:
                    minStep = step
                    return 0

                ans = float("inf")
                for size in range(getMaxValidSize(j), 0, -1):                    
                    setHeight(j, size, size)
                    ans = min(ans, recur(i, j + size, step + 1) + 1)
                    setHeight(j, size, -size)

                memo[key] = ans

            return memo[key]
        
        return recur(0, 0, 0)