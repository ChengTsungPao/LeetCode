class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:

        n_str = str(n)
        m = len(n_str)        
        
        isIncrease = True
        for i in range(1, m):
            if n_str[i] < n_str[i - 1]:
                isIncrease = False
                
        if isIncrease:
            return n
        
        ans = 0
        for i in range(m):
            if int(n_str[i]) == 0:
                continue
            
            number = str(int(n_str[i]) - 1)
            
            for k in range(i - 1, -1, -1):
                number = min(n_str[k], number[0]) + number
            
            number += (m - i - 1) * "9"
            ans = max(ans, int(number))

        return ans