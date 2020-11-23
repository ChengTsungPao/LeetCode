class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = s * (numRows == 1)
        jump = (numRows - 1) * 2, 0
        for index in range(len(ans), numRows):
            flag = True
            while index < len(s):
                ans += s[index]
                if (flag and jump[0] != 0) or jump[1] == 0:
                    flag = False
                    index += jump[0]
                else:
                    flag = True
                    index += jump[1]
            jump = jump[0] - 2, jump[1] + 2
        return ans