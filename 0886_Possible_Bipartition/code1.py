class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        for node1, node2 in dislikes:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        color = {}
        def bfs(node):
            if node in color:
                return True
            
            color[node] = True
            que = collections.deque([node])
            
            while que:
                node = que.pop()
                
                for nextNode in graph[node]:
                    if nextNode in color:
                        if color[node] == color[nextNode]:
                            return False
                        continue
                        
                    color[nextNode] = not color[node]
                    que.appendleft(nextNode)
                    
            return True
        
        for node in range(1, n + 1):
            if bfs(node) == False:
                return False
            
        return True