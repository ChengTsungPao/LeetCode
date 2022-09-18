class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
        n = str(n)
        stack = []
        
        for digit in n[::-1]:
            if stack and int(stack[-1]) <= int(digit) - 1:
                stack = [str(int(digit) - 1)]
            else:
                stack.append(digit)

        return int("".join(stack[::-1]) + "9" * (len(n) - len(stack)))