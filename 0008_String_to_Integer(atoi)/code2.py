class Solution:
    def myAtoi(self, s: str) -> int:
        
        # 去除開頭空白
        s = s.lstrip()
        
        # 開頭連續符號
        if len(s) >= 2 and not s[0].isdigit() and not s[1].isdigit():
            return 0
        
        # 取得數值部分
        isdigit = False
        valueString = ""
        for ch in s:
            if isdigit == False and (ch == "-" or ch == "+"):
                valueString += ch
            elif ch.isdigit():
                valueString += ch
                isdigit = True
            else:
                break
        
        # 字串數值無效
        if valueString == "" or valueString == "+" or valueString == "-":
            return 0
            
        # 轉換成整數
        ans = int(valueString)
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif ans < -2 ** 31:
            return -2 ** 31
        else:
            return ans