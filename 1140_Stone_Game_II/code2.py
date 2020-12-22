class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        def recur(piles, index, M, who, memo = {}):
            key = (index, M, who)
            if key not in memo:
                if len(piles) <= index:
                    return 0
                if who:
                    memo[key] = -float("inf")
                    for i in range(1, 2 * M + 1):
                        memo[key] = max(memo[key], recur(piles, index + i, max(M, i), not who, memo) + sum(piles[index : index + i]))
                else:
                    memo[key] = float("inf")
                    for i in range(1, 2 * M + 1):
                        memo[key] = min(memo[key], recur(piles, index + i, max(M, i), not who, memo))
            return memo[key] 
        
        return recur(piles, 0, 1, True)