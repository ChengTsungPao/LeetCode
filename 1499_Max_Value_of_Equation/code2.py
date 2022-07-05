class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:

        # yi + yj + |xi - xj| = (yi - xi) + (yj + xj)

        ans = -float("inf")
        que = collections.deque()

        for x, y in points:
            
            while que and x - que[0][1] > k:
                que.popleft()

            if que:
                ans = max(ans, que[0][0] + (y + x))
                
            while que and que[-1][0] <= y - x:
                que.pop()
                
            que.append((y - x, x))

        return ans