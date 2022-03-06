class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        # 除了邊邊的杯子外，每個杯子的來源有兩個
        
        memo = {}
        def recur(row, col):
            
            if (row, col) not in memo:
            
                if row < 0:
                    return poured

                if col < 0 or col > row:
                    return 0

                memo[row, col] = max(0, recur(row - 1, col) / 2 + recur(row - 1, col - 1) / 2 - 1)
            
            return memo[row, col]

        ans = recur(query_row - 1, query_glass) / 2 + recur(query_row - 1, query_glass - 1) / 2
        return ans if ans < 1 else 1