class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs) // 2
        
        @functools.lru_cache(None)
        def recur(idx, A, B): # A: goes to city A, B: goes to city B (B = idx - A)
            if A > n or B > n:
                return float("inf")
            elif idx >= n * 2:
                return 0
            return min(costs[idx][0] + recur(idx + 1, A + 1, B), costs[idx][1] + recur(idx + 1, A, B + 1))
        
        return recur(0, 0, 0)