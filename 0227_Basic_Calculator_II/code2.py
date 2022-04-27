class Solution:
    def calculate(self, s: str) -> int:
        
        def convert(s):
            ret = []
            for ch in s:
                if ch == " ":
                    continue
                if ret and ret[-1].isdigit() and ch.isdigit():
                    ret[-1] += ch
                else:
                    ret.append(ch)
            return ret
        
        def calculate(num1, num2, symbol):
            if symbol == "+":
                return str(int(num1) + int(num2))
            elif symbol == "-":
                return str(int(num1) - int(num2))
            elif symbol == "*":
                return str(int(num1) * int(num2))
            else:
                return str(int(num1) // int(num2))
        
        stack = []
        for ch in convert(s):
            if stack and (stack[-1] == "*" or stack[-1] == "/"):
                symbol = stack.pop()
                num1 = stack.pop()
                num2 = ch
                ch = calculate(num1, num2, symbol)
            stack.append(ch)
            
        for ch in stack.copy():
            if stack and (stack[-1] == "+" or stack[-1] == "-"):
                symbol = stack.pop()
                num1 = stack.pop()
                num2 = ch
                ch = calculate(num1, num2, symbol)
            stack.append(ch)
            
        return int(stack[-1])