class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        '''
        利用index避免重複的情形產生，再用i - 1往前計算先前沒算到的operation
        '''
        
        def splitExpression(expression):
            symbol = []
            number = []
            
            tmp = ""
            for s in expression:
                if s.isdigit():
                    tmp += s
                else:
                    number.append(int(tmp))
                    symbol.append(s)
                    tmp = ""
                    
            number.append(int(tmp))
            return number, symbol
        
        
        def cal(a, b, s):
            if s == "-":
                return a - b
            elif s == "+":
                return a + b
            else:
                return a * b


        def recur(number, symbol, index, abc = 0):
            nonlocal ans
            
            if len(number) == 1:
                ans.append(number[0])
                return 
            
            for i in range(index, len(number) - 1):
                a, b = number[i], number[i + 1]
                s = symbol[i]
                
                num = cal(a, b, s)
                number[i] = num
                del number[i + 1]
                del symbol[i]
                
                recur(number, symbol, max((i - 1), 0), 1)
                
                number[i] = a
                number.insert(i + 1, b)
                symbol.insert(i, s)

        
        number, symbol = splitExpression(expression)
        
        ans = []
        recur(number, symbol, 0)
                
        return ans