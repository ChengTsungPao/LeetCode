class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def calculate(num1, num2, opr):
            num1, num2 = int(num1), int(num2)
            if opr == "+":
                return str(num1 + num2)
            if opr == "-":
                return str(num1 - num2)
            if opr == "*":
                return str(num1 * num2)
            else:
                return str(int(num1 / num2))
            
        stack = []
        
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(token)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(calculate(num1, num2, token))
                
        return int(stack[0])