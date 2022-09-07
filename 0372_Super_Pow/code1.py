class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        MOD = 1337
        
        def myPow(a, b):
            if b == 0:
                return 1

            ans = a
            times = 1
            while times * 2 <= b:
                ans = (ans * ans) % MOD
                times *= 2
                
            return (ans * myPow(a, b - times)) % MOD
        
        ans = 1
        for d in b:
            ans = (myPow(ans, 10) * myPow(a, d)) % MOD
        
        return ans