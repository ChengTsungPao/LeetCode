class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s += "#"
        
        for i in range(len(s)):
            if s[i] == " ":
                continue
                
            if s[i].isdigit():
                if len(stack) >= 1 and stack[-1].isdigit():
                    stack[-1] += s[i]
                else:
                    stack.append(s[i])
                continue
                    
            if len(stack) >= 3:
                if stack[-2] == "*":
                    result = str(int(stack[-3]) * int(stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack[-1] = result
                elif stack[-2] == "/":
                    result = str(int(stack[-3]) // int(stack[-1]))
                    stack.pop()
                    stack.pop()
                    stack[-1] = result
                    
            stack.append(s[i])

        ans = int(stack[0])
        for i in range(2, len(stack) - 1, 2):
            if stack[i - 1] == "+":
                ans += int(stack[i])
            else:
                ans -= int(stack[i])
                
        return ans