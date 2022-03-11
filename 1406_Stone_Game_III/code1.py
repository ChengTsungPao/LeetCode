class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        n = len(stoneValue)

        memo = {}
        def recur(index, who):
            if (index, who) not in memo:

                if index >= n:
                    return 0

                if who:
                    ans = -float("inf")
                    for i in range(1, 3 + 1):
                        ans = max(ans, recur(index + i, not who) + sum(stoneValue[index: index + i]))
                else:
                    ans = float("inf")
                    for i in range(1, 3 + 1):
                        ans = min(ans, recur(index + i, not who) - sum(stoneValue[index: index + i]))

                memo[index, who] = ans

            return memo[index, who]
            

        score = recur(0, True)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"