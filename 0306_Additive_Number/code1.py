class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        # 註: 開頭是零只可能 number = "0"
        
        def isAdditive(num1, num2, otherNum):

            while otherNum:
                
                num1, num2 = num2, str(int(num1) + int(num2))
                newNum, otherNum = otherNum[:len(num2)], otherNum[len(num2):]
                
                if num2 != newNum:
                    return False
                
            return True
        
        if len(num) < 3: return False
        elif int(num) == 0: return True
        
        for length1 in range(1, len(num) // 2 + 1):
            
            for length2 in range(1, len(num) // 2 + 1):
                
                i, j = length1, length1 + length2
                length3 = len(num) - j
                
                if (length1 != 1 and num[0] == "0") or \
                   (length2 != 1 and num[i] == "0") or \
                   (length3 == 0 or  num[j] == "0"):
                    continue
                    
                if isAdditive(num[:i], num[i:j], num[j:]):
                    return True
                
        return False
