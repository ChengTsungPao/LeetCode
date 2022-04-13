class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # 建立九九乘法表 (單一數字互乘)
        mulTable = {}
        for i in range(9 + 1):
            for j in range(9 + 1):
                mulTable[str(i), str(j)] = i * j
        
        # 計算一組數字和一個數字的乘法結果
        def mul(num, digit):
            s = 0
            m = 1
            for i in range(len(num)):
                s += mulTable[num[~i], digit] * m
                m *= 10
            return s
        
        # 計算一組數字和一組數字的乘法結果
        s = 0
        m = 1
        for i in range(len(num2)):
            s += mul(num1, num2[~i]) * m
            m *= 10                
        
        return str(s)