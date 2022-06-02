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
        
        ans = float("inf")
        def recur(i, j, step):
            nonlocal ans
            
            if step >= ans:
                return
            
            i, j = convertPos(i, j)

            if i >= n:
                ans = step
                return

            for size in range(getMaxValidSize(j), 0, -1):
                setHeight(j, size, size)
                recur(i, j + size, step + 1)
                setHeight(j, size, -size)

        recur(0, 0, 0)
        
        return ans