class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n = len(piles)

        memo = {}
        def recur(index, M, who):
            if (index, M, who) not in memo:

                if index >= n:
                    return 0

                if who:
                    ans = -float("inf")
                    for x in range(1, 2 * M + 1):
                        ans = max(ans, recur(index + x, max(x, M), not who) + sum(piles[index: index + x]))
                else:
                    ans = float("inf")
                    for x in range(1, 2 * M + 1):
                        ans = min(ans, recur(index + x, max(x, M), not who))

                memo[index, M, who] = ans

            return memo[index, M, who]

        return recur(0, 1, True)