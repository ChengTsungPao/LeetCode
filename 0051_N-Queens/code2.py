class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # 將坐標軸旋轉45度，觀察row和col是否有訪問過
        
        def transfer(i, j):
            rotate = complex(i, j) * complex(1, 1)
            return int(rotate.real), int(rotate.imag)
            
        def recur(row, colSet = set(range(n)), found = {"rotateRow": set(), "rotateCol": set()}):
            
            if row == n:
                return [[]]

            ans = []

            for col in list(colSet):

                rotateRow, rotateCol = transfer(row, col)
                
                if rotateRow in found["rotateRow"] or rotateCol in found["rotateCol"]:
                    continue
                
                colSet.remove(col)
                found["rotateRow"].add(rotateRow)
                found["rotateCol"].add(rotateCol)
                
                for sol in recur(row + 1, colSet, found):
                    ans.append(["." * col + "Q" + "." * (n - col - 1)] + sol)
                    
                colSet.add(col)
                found["rotateRow"].remove(rotateRow)
                found["rotateCol"].remove(rotateCol)
                
            return ans
        
        return recur(0)
