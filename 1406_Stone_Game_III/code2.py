class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)

        memo = {}
        def recur(index):
            if (index) not in memo:

                if index >= n:
                    return 0

                ans = -float("inf")
                for i in range(1, 3 + 1):
                    ans = max(ans, sum(stoneValue[index: index + i]) - recur(index + i))

                memo[index] = ans

            return memo[index]
        

        score = recur(0)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"