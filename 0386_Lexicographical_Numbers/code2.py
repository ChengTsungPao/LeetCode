class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        ans = []
        
        num = 1
        for _ in range(n): 
            ans.append(num)
                
            if num * 10 <= n:
                num *= 10
            elif num % 10 != 9 and num + 1 <= n:
                num += 1
            else:
                while (num // 10) % 10 == 9:
                    num //= 10
                num = num // 10 + 1
            
        return ans