class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # Topological Sorting
        
        if n <= 2:
            return list(range(n))
        
        graph = collections.defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
              
        count = n
        while count > 2:
            count -= len(leaves)
            
            newLeaves = []
            for leaf in leaves:
                newLeaf = graph[leaf].pop()
                graph[newLeaf].remove(leaf)
                
                if len(graph[newLeaf]) == 1:
                    newLeaves.append(newLeaf)
                    
            leaves = newLeaves
            
        return leaves