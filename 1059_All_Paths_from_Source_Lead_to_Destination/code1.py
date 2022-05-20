class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = collections.defaultdict(list)
        for node, nextNode in edges:
            graph[node].append(nextNode)
            
            
        if graph[destination]:
            return False
        
        memo = set()
        visited = set()
        def recur(node):
            
            if node not in memo:
            
                if node == destination:
                    return True
                if node in visited or not graph[node]:
                    return False
                
                visited.add(node)
                for nextNode in graph[node]:
                    if not recur(nextNode):
                        return False
                visited.remove(node)
                    
                memo.add(node)
            
            return True
        
        return recur(source)