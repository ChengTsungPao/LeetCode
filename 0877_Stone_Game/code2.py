class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        def recur(piles, i, j, who, memo = {}):
            if (i, j) not in memo:
                if i > j:
                    return 0
                if who:
                    memo[(i, j)] = max(recur(piles, i + 1, j, not who, memo) + piles[i], recur(piles, i, j - 1, not who, memo) + piles[j])
                else:
                    memo[(i, j)] = min(recur(piles, i + 1, j, not who, memo) - piles[i], recur(piles, i, j - 1, not who, memo) - piles[j])
            return memo[(i, j)] 
        
        return recur(piles, 0, len(piles) - 1, True) > 0