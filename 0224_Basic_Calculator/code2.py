class Solution:
    def calculate(self, s: str) -> int:
        
        def cal(num1, num2, kind):
            if kind == "+":
                return str(int(num1) + int(num2))
            else:
                return str(int(num1) - int(num2))
            
        def convert(s):
            ret = []
            for ch in s:
                if ch == " ":
                    continue
                if ret and ret[-1].isdigit() and ch.isdigit():
                    ret[-1] += ch
                elif (ch == "+" or ch == "-") and (len(ret) == 0 or ret[-1] == "("):
                    ret.append("0")
                    ret.append(ch)
                else:
                    ret.append(ch)
            return ret

        stack = []
        for ch in convert("(" + s + ")")[::-1]:   
            
            if stack and ch == "(":
                ch = stack.pop()
                while stack[-1] != ")":
                    kind = stack.pop()
                    num = stack.pop()
                    ch = cal(ch, num, kind)  
                stack.pop()
            
            stack.append(ch)
            
        return int(stack[0])