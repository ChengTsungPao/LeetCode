class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        n = len(price)
        m = len(special)
        
        def buy(s, needs, target):
            for i in range(n):
                needs[i] += s[i] * target
        
        memo = {}
        def recur(index, needs):
            
            key = str(needs) + "_" + str(index)
            
            if key not in memo:

                if min(needs) < 0:
                    return float("inf")
                elif sum(needs) == 0:
                    return 0

                ans = sum([price[i] * needs[i] for i in range(n)])
                for i in range(index, m):
                    buy(special[i], needs, -1)
                    ans = min(ans, special[i][-1] + recur(i, needs))
                    buy(special[i], needs,  1)
                    
                memo[key] = ans
                
            return memo[key]
        
        return recur(0, needs)