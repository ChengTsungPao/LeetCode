class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        n = len(num)
        
        count = 0
        stack = []
        for digit in num:
            while stack and stack[-1] > digit and count < k:
                stack.pop()
                count += 1
            
            stack.append(digit)

        ans = ""
        for digit in "".join(stack[: n - k]):
            if ans == "" and digit == "0":
                continue
            ans += digit
        
        return ans if ans != "" else "0"