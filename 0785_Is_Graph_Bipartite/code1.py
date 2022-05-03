class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        def bfs(node):
            if node in color:
                return True
            
            que = collections.deque([node])
            color[node] = True
            while que:
                node = que.pop()
                
                for nextNode in graph[node]:
                    if nextNode in color:
                        if color[nextNode] == color[node]:
                            return False
                        continue
                    
                    color[nextNode] = not color[node]
                    que.appendleft(nextNode)
                    
            return True
        
        for node in range(len(graph)):
            if bfs(node) == False:
                return False
            
        return True