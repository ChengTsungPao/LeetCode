class Solution:
    def lastRemaining(self, n: int) -> int:
        
        # 0: (number + 1) // 2
        # 1: number // 2
        
        oprs = []
        while n > 1:
            if len(oprs) % 2 == 0:
                oprs.append(1)
            else:
                oprs.append(n % 2)
            n //= 2
        
        ans = 1
        for opr in oprs[::-1]:
            if opr:
                ans = ans * 2
            else:
                ans = ans * 2 - 1
                
        return ans 