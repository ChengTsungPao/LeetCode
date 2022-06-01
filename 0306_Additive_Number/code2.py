class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        n = len(num)
        
        def isValid(num):
            return not (len(num) >= 2 and num[0] == "0")
        
        def simulation(num1, num2):
            if not (isValid(num1) and isValid(num2)):
                return False
            
            index = len(num1) + len(num2)
            while index < n:
                num3 = str(int(num1) + int(num2))
                length = len(num3)
                if num[index: index + length] != num3:
                    return False
                
                num1, num2 = num2, num3
                index += length
                
            return True
        
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                num1 = num[:i]
                num2 = num[i: j]
                if simulation(num1, num2):
                    return True
                
        return False