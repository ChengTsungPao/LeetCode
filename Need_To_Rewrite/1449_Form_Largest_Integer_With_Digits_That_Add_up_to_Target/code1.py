class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = {}
        if set(cost) == set([1]):
            return str(len(cost)) * target
        def dfs(data, cost, str_):
            if cost not in dp:
                if cost == target:
                    return str_
                elif cost > target:
                    return "0"
                max_ = "0"
                for i in range(len(data)):
                    tmp = dfs(data, cost + data[i], str_ + str(i + 1))
                    if tmp != "0":
                        max_ = str(max(int(max_), int(tmp[len(str_):])))
                dp[cost] = max_
            if dp[cost] == "0":
                return "0"
            else:
                return str_ + dp[cost]              
        return dfs(cost, 0, "")
