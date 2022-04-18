class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        
        def countTwoFive(num):
            count = [0, 0]
            while num % 2 == 0:
                count[0] += 1
                num //= 2
            while num % 5 == 0:
                count[1] += 1
                num //= 5
            return count
        
        def addCount(count1, count2):
            return [count1[0] + count2[0], count1[1] + count2[1]]
        
        
        m = len(grid)
        n = len(grid[0])
        
        # count two and five
        mid = [[[0, 0] for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):   
                mid[i][j] = countTwoFive(grid[i][j])
                
                
        # prefixSum and suffixSum
        left = [[[0, 0] for _ in range(n)] for _ in range(m)]
        right = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            count = [0, 0]
            for j in range(n):
                left[i][j] = count
                count = addCount(count, mid[i][j])
                
            count = [0, 0]
            for j in range(n - 1, -1, -1):
                right[i][j] = count
                count = addCount(count, mid[i][j])
                
        up = [[[0, 0] for _ in range(n)] for _ in range(m)]
        down = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        for j in range(n):
            count = [0, 0]
            for i in range(m):
                up[i][j] = count
                count = addCount(count, mid[i][j])
                
            count = [0, 0]
            for i in range(m - 1, -1, -1):
                down[i][j] = count
                count = addCount(count, mid[i][j])
                
        
        # calculate answer
        ans = 0
        for i in range(m):
            for j in range(n):
                v = mid[i][j]
                l, r, u, d = left[i][j], right[i][j], up[i][j], down[i][j]
                for a, b in [(l, r), (l, u), (l, d), (r, u), (r, d), (u, d)]:
                    s = addCount(a, b)
                    s = addCount(v, s)
                    ans = max(ans, min(s))

        return ans
        