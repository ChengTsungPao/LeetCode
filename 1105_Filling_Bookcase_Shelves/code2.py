class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        n = len(books)
        
        dp = [0] * (n + 1)
        for i in range(n - 1, -1 ,-1):
            
            minHeight = float("inf")
            width = height = 0
            for j in range(i, n):
                w, h = books[j]

                width += w
                if width > shelfWidth:
                    break

                height = max(height, h)
                minHeight = min(minHeight, height + dp[j + 1])

            dp[i] = minHeight
            
        return dp[0]