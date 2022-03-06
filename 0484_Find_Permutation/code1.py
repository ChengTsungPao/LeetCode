class Solution:
    def findPermutation(self, s: str) -> List[int]:
        
        n = len(s)
        s += "I" if s[-1] == "D" else "D"
        
        # 建立最小數組
        ans = list(range(1, n + 2))
        
        # 遇到連續"D"的區間就reverse
        i = 0
        for j in range(1, n + 1):
            if s[j - 1] != s[j]:
                if s[j - 1] == "D":
                    ans[i: j + 1] = reversed(ans[i: j + 1])
                i = j
        
        return ans