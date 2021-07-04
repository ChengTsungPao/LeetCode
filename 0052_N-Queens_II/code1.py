class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def recur(row, found):
            
            if row == n:
                return 1

            ans = 0

            for col in range(n):

                is_restrict = False
                for i, j in found:
                    if col == j or abs(row - i) == abs(col - j):
                        is_restrict = True
                        break

                if is_restrict:
                    continue

                found.add((row, col))
                ans += recur(row + 1, found)
                found.remove((row, col))
                
            return ans
        
        return recur(0, set())
