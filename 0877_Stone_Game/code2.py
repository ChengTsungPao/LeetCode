class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}
        def recur(i, j, who):
            if (i, j) not in memo:

                if i > j:
                    return 0

                if who:
                    ans = max(recur(i + 1, j, not who) + piles[i], recur(i, j - 1, not who) + piles[j])
                else:
                    ans = min(recur(i + 1, j, not who) - piles[i], recur(i, j - 1, not who) - piles[j])

                memo[i, j] = ans

            return memo[i, j]

        return recur(0, len(piles) - 1, True) >= 0