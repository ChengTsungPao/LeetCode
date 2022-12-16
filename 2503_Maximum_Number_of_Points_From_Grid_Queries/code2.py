class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        query_sorted = sorted(queries)
        
        m = len(grid)
        n = len(grid[0])
        
        def bfs(query, edge, minNextEdge = [0]):

            newVisitedPos = 0
            
            while edge and edge[0][0] < query:
                _, x, y = heapq.heappop(edge)
                newVisitedPos += 1
                
                for x_, y_ in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    if not (0 <= x_ < m and 0 <= y_ < n) or grid[x_][y_] == "#":
                        continue

                    heapq.heappush(edge, (grid[x_][y_], x_, y_))
                    grid[x_][y_] = "#"
                    
            return newVisitedPos
        
        ans = []
        
        edge = [(grid[0][1], 0, 1), (grid[1][0], 1, 0)]
        heapq.heapify(edge)
        val = grid[0][0]
        grid[0][0] = grid[0][1] = grid[1][0] = "#"
        
        for query in query_sorted:
            if query <= val:
                ans.append(0)
            else:
                count = bfs(query, edge) + (1 if not ans or ans[-1] == 0 else ans[-1])
                ans.append(count)
                
        ans_dict = {}
        for query, count in zip(query_sorted, ans):
            ans_dict[query] = count
            
        return [ans_dict[query] for query in queries]