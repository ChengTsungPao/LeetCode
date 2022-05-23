class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        ans = 0
        height = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    height[j] += 1
                else:
                    height[j] = 0
                    
            for w, h in enumerate(sorted(height, reverse = True)):
                ans = max(ans, (w + 1) * h)
                
        return ans