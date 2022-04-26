class Solution:
    def romanToInt(self, s: str) -> int:
        
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        def cal(num):
            ret = table[num[-1]]
            for i in range(len(num) - 1):
                ret -= table[num[i]]
            return ret

        
        n = len(s)
        
        ans = 0
        num = [s[0]]
        for i in range(1, n):
            if table[num[-1]] >= table[s[i]]:
                ans += cal(num)
                num = []
            num.append(s[i])
        ans += cal(num)
        
        return ans