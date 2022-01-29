class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        import numpy as np
        
        n = len(img1)
        img2 = np.pad(img2, n - 1)
        
        ans = 0
        for i in range(len(img2) - n + 1):
            for j in range(len(img2) - n + 1):
                ans = max(ans, np.sum(img2[i: i + n, j: j + n] * img1))
        
        return ans