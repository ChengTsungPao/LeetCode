class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        curK = k
        stack = []
        for n in num:            
            while stack and stack[-1] > n and curK > 0:
                stack.pop()
                curK -= 1
                
            stack.append(n)
        
        ans = "".join(stack[:len(num) - k])          
        
        return str(int(ans)) if ans != "" else "0"  