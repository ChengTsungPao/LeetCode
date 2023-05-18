class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # concept: topological sort without cycle
        
        parent = collections.defaultdict(int)
        for node, nextNode in edges:
            parent[nextNode] += 1
                    
        return [node for node in range(n) if parent[node] == 0]