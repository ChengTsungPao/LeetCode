class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2
        
        n = len(graph)
        color = [WHITE] * n
        
        def dfs(node):
            if color[node] == GRAY:
                return False
            elif color[node] == BLACK:
                return True
            
            color[node] = GRAY
            for nextNode in graph[node]:
                if color[nextNode] == BLACK:
                    continue
                    
                if not dfs(nextNode):
                    return False
            color[node] = BLACK
            
            return True

        return [node for node in range(n) if dfs(node)]