class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:                
        
        def collide_time(i, j):
            return (cars[j][0] - cars[i][0]) / (cars[i][1] - cars[j][1])
        
        def lower_time(i, j):
            if j == 0:
                return float("inf"), "#"
            elif dp[j][0] < collide_time(i, j):
                time, index = collide_time(i, dp[j][1]), dp[j][1]
                time_next, index_next = lower_time(i, dp[j][1])
                if time <= time_next:
                    return time, index
                else:
                    return time_next, index_next
            else:
                return collide_time(i, j), j

        stack = []
        next_smaller_speed = collections.defaultdict(int)
        for i in range(len(cars)):
            while stack and stack[-1][1] > cars[i][1]:
                next_smaller_speed[stack[-1][0]] = i
                stack.pop()
            stack.append((i, cars[i][1]))                    

        dp = {len(cars) - 1: (float("inf"), len(cars) - 1)}
        for i in range(len(cars) - 1, -1, -1):
            dp[i] = lower_time(i, next_smaller_speed[i])

        ans = []
        for i in range(len(dp)):
            if dp[i][0] == float("inf"):
                ans.append(-1)
            else:
                ans.append(dp[i][0])
        
        return ans
