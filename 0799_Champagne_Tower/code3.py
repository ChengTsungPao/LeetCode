class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        memo = {}
        def recur(i, j):
            
            if (i, j) not in memo:
            
                if i == 0 and j == 0:
                    return poured
                elif j < 0 or j >= i + 1:
                    return 0
                
                left  = max((recur(i - 1, j - 0) - 1) / 2, 0)
                right = max((recur(i - 1, j - 1) - 1) / 2, 0)
                
                memo[i, j] = left + right
            
            return memo[i, j]
        
        if query_row == query_row == 0:
            ans = poured
        else:
            left  = max((recur(query_row - 1, query_glass - 0) - 1) / 2, 0)
            right = max((recur(query_row - 1, query_glass - 1) - 1) / 2, 0)
            ans = left + right
        
        return ans if ans <= 1 else 1