class Solution:
    def totalNQueens(self, n: int) -> int:
        
        # 將坐標軸旋轉45度，觀察row和col是否有訪問過，藉此來判斷斜的方向是否相衝
        
        def transfer(i, j):
            rotate = complex(i, j) * complex(1, 1)
            return int(rotate.real), int(rotate.imag)
            
        def recur(row, colSet = set(range(n)), found = {"rotateRow": set(), "rotateCol": set()}):
            
            if row == n:
                return 1

            ans = 0

            for col in list(colSet):

                rotateRow, rotateCol = transfer(row, col)
                
                if rotateRow in found["rotateRow"] or rotateCol in found["rotateCol"]:
                    continue
                
                colSet.remove(col)
                found["rotateRow"].add(rotateRow)
                found["rotateCol"].add(rotateCol)
                
                ans += recur(row + 1, colSet, found)
                    
                colSet.add(col)
                found["rotateRow"].remove(rotateRow)
                found["rotateCol"].remove(rotateCol)
                
            return ans
        
        return recur(0)
