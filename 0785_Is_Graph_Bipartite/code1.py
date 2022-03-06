class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:        
        colors = {}
        
        def bfs(node):
            if node in colors:
                return True
            
            que = collections.deque([(node, True)])
            while que:
                node, color = que.pop()
                colors[node] = color

                for nextNode in graph[node]:
                    if nextNode in colors:
                        if colors[nextNode] == color:
                            return False
                        else:
                            continue
                    else:
                        que.appendleft((nextNode, not color))
                        
            return True
                        
        for node in range(len(graph)):
            if bfs(node) == False:
                return False
                    
        return True