class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        memo = {}
        def recur(i, j, step):
            
            if (i, j, step) not in memo:
            
                if not (0 <= i < n and 0 <= j < n):
                    return 0
                elif step == 0:
                    return 1

                ret = 0
                for i_, j_ in [(i+2,j+1),(i+2,j-1),(i-2,j+1),(i-2,j-1),(i+1,j+2),(i-1,j+2),(i+1,j-2),(i-1,j-2)]:
                    ret += recur(i_, j_, step - 1) / 8
                    
                memo[i, j, step] = ret
                
            return memo[i, j, step]
        
        return recur(row, column, k)