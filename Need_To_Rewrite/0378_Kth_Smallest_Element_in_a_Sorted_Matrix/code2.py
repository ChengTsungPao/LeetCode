class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        i, j, n, heap, dp = 0, 0, len(matrix), [(matrix[0][0], 0, 0)], {(0, 0): False}
        
        while heap and k > 0:
            ans, i, j = heapq.heappop(heap)
            dp[i, j] = True
            if (i + 1 < n and (i + 1, j) not in dp) and (j - 1 <= 0 or ((i + 1, j - 1) in dp and dp[i + 1, j - 1])):
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
                dp[i + 1, j] = False
            if (j + 1 < n and (i, j + 1) not in dp) and (i - 1 <= 0 or ((i - 1, j + 1) in dp and dp[i - 1, j + 1])):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
                dp[i, j + 1] = False  
            k -= 1
            
        return ans