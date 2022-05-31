class Solution:
    def soupServings(self, n: int) -> float:
        
        if n >= 5000:
            return 1
        
        soup = [
            [100,  0],
            [ 75, 25],
            [ 50, 50],
            [ 25, 75]
        ]
        
        memo = {}
        def recur(A, B):
            
            if (A, B) not in memo:
            
                if A <= 0 and B <= 0:
                    return 0.5
                elif A <= 0:
                    return 1
                elif B <= 0:
                    return 0         

                ans = 0
                for soupA, soupB in soup:
                    ans += 0.25 * recur(A - soupA, B - soupB)
                    
                memo[A, B] = ans
                    
            return memo[A, B]

        return recur(n, n)