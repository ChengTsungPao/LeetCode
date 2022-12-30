class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        MOD = pow(10, 9) + 7
        n = len(locations)
        
        @functools.lru_cache(None)
        def recur(i, fuel):
            if fuel == 0:
                return (i == finish) * 1
            elif fuel < 0:
                return 0
            
            ans = (i == finish) * 1
            for j in range(n):
                if j != i:
                    cost = abs(locations[j] - locations[i])
                    ans += recur(j, fuel - cost)
            return ans
        
        return recur(start, fuel) % MOD