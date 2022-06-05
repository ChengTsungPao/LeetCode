class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        candidate = set()
        graph = collections.defaultdict(set)
        for node, nextNode in connections:
            candidate.add(tuple(sorted([node, nextNode])))
            graph[node].add(nextNode)
            graph[nextNode].add(node)
            
        
        rank = [-2] * n
        def dfs(node, depth):
            
            if rank[node] >= 0:
                return rank[node]

            rank[node] = depth
            
            minRank = n
            for nextNode in graph[node]:
                if rank[nextNode] == depth - 1:
                    continue
                
                retRank = dfs(nextNode, depth + 1)
                if retRank <= depth:
                    edge = tuple(sorted([node, nextNode]))
                    candidate.remove(edge)
                    
                minRank = min(minRank, retRank)
                
            rank[node] = n
            
            return minRank
        
        dfs(0, 0)
        return list(candidate)