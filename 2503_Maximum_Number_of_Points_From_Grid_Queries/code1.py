class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        query_sorted = sorted(queries)
        
        m = len(grid)
        n = len(grid[0])
        
        def bfs(query, edge, minNextEdge = [0]):
            # if minNextEdge[0] >= query:
            #     return 0

            que = collections.deque([edge.pop() for _ in range(len(edge))])
            grid[0][0] = "#"
            newVisitedPos = 0
            
            while que:
                x, y = que.popleft()

                maxNeiVal = 0
                for x_, y_ in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    if not (0 <= x_ < m and 0 <= y_ < n) or grid[x_][y_] == "#":
                        continue
                        
                    maxNeiVal = max(maxNeiVal, grid[x_][y_])
                    
                    if query <= grid[x_][y_]:
                        continue

                    grid[x_][y_] = "#"
                    que.append((x_, y_))
                    newVisitedPos += 1
                    
                if maxNeiVal >= query:
                    # minNextEdge[0] = min(minNextEdge[0], maxNeiVal)
                    edge.add((x, y))
                    
            return newVisitedPos
        
        ans = []
        edge = set([(0, 0)])
        leftRightVal = grid[0][0]
        for query in query_sorted:
            if query <= leftRightVal:
                ans.append(0)
            else:
                count = bfs(query, edge) + (1 if not ans or ans[-1] == 0 else ans[-1])
                ans.append(count)
                
        ans_dict = {}
        for query, count in zip(query_sorted, ans):
            ans_dict[query] = count
            
        return [ans_dict[query] for query in queries]