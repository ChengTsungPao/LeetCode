class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        status = {0 : 0, 1 : 0}
        costs.sort(key = lambda x : abs(x[0] - x[1]), reverse = True)
        ans = 0
        for cost in costs:
            if status[0] == len(costs) // 2:
                ans += cost[1]
            elif status[1] == len(costs) // 2:
                ans += cost[0]
            elif cost[0] - cost[1] > 0:
                status[1] += 1
                ans += cost[1]
            elif cost[0] - cost[1] < 0:
                status[0] += 1
                ans += cost[0]
            else:
                ans += cost[0]
        return ans