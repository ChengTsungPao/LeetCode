class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def recur(stoneValue, index, who, memo = {}):
            key = (index, who)
            if key not in memo:
                if len(stoneValue) <= index:
                    return 0
                if who:
                    memo[key] = -float("inf")
                    for i in range(1, 3 + 1):
                        memo[key] = max(memo[key], recur(stoneValue, index + i, not who, memo) + sum(stoneValue[index : index + i]))
                else:
                    memo[key] = float("inf")
                    for i in range(1, 3 + 1):
                        memo[key] = min(memo[key], recur(stoneValue, index + i, not who, memo) - sum(stoneValue[index : index + i]))
            return memo[key]
        
        ans = recur(stoneValue, 0, True)

        if ans > 0:
            return "Alice"
        elif ans < 0:
            return "Bob"
        else:
            return "Tie"