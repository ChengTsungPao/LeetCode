class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        dominoes = "L" + dominoes + "R"
        n = len(dominoes)
        
        ans = ""
        i = 0
        for j in range(1, n):
            if dominoes[j] == ".":
                continue
                
            L_Direction, R_Direction = dominoes[i], dominoes[j]
            if L_Direction == R_Direction:
                ans += L_Direction * (j - i)
            elif L_Direction == "L" and R_Direction == "R":
                ans += L_Direction + "." * (j - i - 1)
            else:
                length = j - i - 1
                ans += L_Direction * (length // 2 + 1) + "." * (length % 2) + R_Direction * (length // 2)
            i = j
                
        return ans[1:]