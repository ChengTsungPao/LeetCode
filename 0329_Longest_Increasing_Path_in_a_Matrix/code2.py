class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])
        
        parent = collections.defaultdict(int)
        graph  = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if not (0 <= x < m and 0 <= y < n) or matrix[i][j] >= matrix[x][y]:
                        continue
                    graph[i, j].append((x, y))
                    parent[x, y] += 1
        
        
        que = collections.deque()
        for i in range(m):
            for j in range(n):
                if parent[i, j] == 0:
                    que.appendleft((i, j))
        
        level = 0
        while que:
            
            newQue = collections.deque()
            while que:
                i, j = que.pop()

                for x, y in graph[i, j]:
                    parent[x, y] -= 1
                    if parent[x, y] == 0:
                        newQue.appendleft((x, y))
                        
            que = newQue
            level += 1
            
        return max(level, 1)