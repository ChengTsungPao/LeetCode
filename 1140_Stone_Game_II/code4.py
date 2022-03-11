class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        # 計算 Alice - Bob 和 Alice + Bob，解出 Alice
        
        n = len(piles)

        memo = {}
        def recur(index, M):
            if (index, M) not in memo:

                if index >= n:
                    return 0

                ans = -float("inf")
                for x in range(1, 2 * M + 1):
                    ans = max(ans, sum(piles[index: index + x]) - recur(index + x, max(x, M)))

                memo[index, M] = ans

            return memo[index, M]

        add = sum(piles)
        sub = recur(0, 1)
        
        return (add + sub) // 2