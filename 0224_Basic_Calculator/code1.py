class Solution:
    def calculateNoParentheses(self, s: str) -> int:
        stack = []
        s += "#"
        
        for i in range(len(s)):                
            if s[i].isdigit():
                if len(stack) >= 1 and (len(stack) == 1 or stack[-1].isdigit()):
                    stack[-1] += s[i]
                else:
                    stack.append(s[i])
            else:    
                stack.append(s[i])

        ans = int(stack[0])
        for i in range(2, len(stack) - 1, 2):
            if stack[i - 1] == "+":
                ans += int(stack[i])
            else:
                ans -= int(stack[i])
                
        return ans 
    
    
    def mergeNum(self, stack: list, result: str) -> str:
        if len(stack) == 0:
            stack.append(result)
            return
        
        opr1, formula1 = stack[-1][-1], stack[-1][:-1]
        opr2, formula2 = result[0], result[1:]
        
        if opr1 == "-" and opr2 == "-":
            stack[-1] = formula1
            stack[-1] += "+" + formula2
        elif opr1 == "+" and opr2 == "-":
            stack[-1] = formula1
            stack[-1] += "-" + formula2
        elif opr1 == "(":
            stack.append(opr2 + formula2)
        else:
            stack[-1] += opr2 + formula2

    
    def calculate(self, s: str) -> int:
        stack = []
        for i in range(len(s)):     
            if s[i] == " ":
                continue            
            
            if s[i] == ")":
                result = str(self.calculateNoParentheses(stack.pop()))
                stack.pop()
                self.mergeNum(stack, result)
                continue
                
            if len(stack) == 0 or stack[-1] == "(" or s[i] == "(":
                stack.append(s[i])
            else:
                stack[-1] += s[i]
       
        return self.calculateNoParentheses(stack[0])