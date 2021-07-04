class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def recur(row, found):
            
            if row == n:
                return [[]]

            ans = []

            for col in range(n):

                is_restrict = False
                for i, j in found:
                    if col == j or abs(row - i) == abs(col - j):
                        is_restrict = True
                        break

                if is_restrict:
                    continue

                found.add((row, col))
                for sol in recur(row + 1, found):
                    ans.append(["." * col + "Q" + "." * (n - col - 1)] + sol)
                found.remove((row, col))
                
            return ans
        
        return recur(0, set())
