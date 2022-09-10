class Solution:
    def totalNQueens(self, n: int) -> int:
        
        col = set()
        diag = set()
        antdiag = set()
        
        def recur(x):
            if x >= n:
                return 1
            
            ans = 0
            for y in range(n):
                if y in col or x - y in diag or x + y in antdiag:
                    continue
                
                col.add(y)
                diag.add(x - y)
                antdiag.add(x + y)
                
                ans += recur(x + 1)
                
                col.remove(y)
                diag.remove(x - y)
                antdiag.remove(x + y)
                
            return ans
        
        return recur(0)