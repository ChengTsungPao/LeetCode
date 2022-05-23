class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        n = len(books)
        
        memo = {}
        def recur(index):
            
            if index not in memo:

                if index >= n:
                    return 0

                ans = float("inf")
                width = height = 0
                for i in range(index, n):
                    w, h = books[i]

                    width += w
                    if width > shelfWidth:
                        break

                    height = max(height, h)
                    ans = min(ans, height + recur(i + 1))
                    
                memo[index] = ans

            return memo[index]
        
        return recur(0)