class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        dominoes = "L" + dominoes + "R"
        n = len(dominoes)
        
        left = [None] * n
        right = [None] * n
        for i in range(n):
            if dominoes[ i] != ".": l = i, dominoes[i] 
            if dominoes[~i] != ".": r = n + (~i), dominoes[~i] 
            left[i], right[~i] = l, r
            
        ans = ["."] * n
        for i in range(n):      
            L_Index, L_Direction = left[i]
            R_Index, R_Direction = right[i]
            if L_Direction == "L" and R_Direction == "R":
                continue
                
            if L_Direction == R_Direction:
                ans[i] = L_Direction
            elif abs(i - L_Index) < abs(i - R_Index):
                ans[i] = L_Direction
            elif abs(i - L_Index) > abs(i - R_Index):
                ans[i] = R_Direction
 
        return "".join(ans[1:-1]) 