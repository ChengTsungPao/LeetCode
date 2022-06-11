class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        n = len(bombs)
        
        def isBomb(bomb1, bomb2):
            x1, y1, r1 = bomb1
            x2, y2, r2 = bomb2
            return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2
        
        graph = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                if isBomb(bombs[i], bombs[j]):
                    graph[i].append(j)
                if isBomb(bombs[j], bombs[i]):
                    graph[j].append(i)

        def dfs(index):
            if visited[index]:
                return 0
            visited[index] = True
            count = 1
            for nextIndex in graph[index]:
                count += dfs(nextIndex)
            return count
        
        ans = 0
        for index in range(n):
            visited = [False] * n
            ans = max(ans, dfs(index))
            
        return ans