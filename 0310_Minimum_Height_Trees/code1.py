class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # Topological Sorting的概念 (依序把只有一個link的node刪除)
        
        graph = collections.defaultdict(set)
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        
        visited = set()
        while len(visited) < n:

            ans = []
            leafs = [] # (leaf, newLeaf)
            for i in range(n):
                if i in visited:
                    continue
                if len(graph[i]) == 0: # leaf
                    ans.append(i)
                    visited.add(i)
                elif len(graph[i]) == 1:
                    ans.append(i)
                    visited.add(i)
                    leafs.append((i, list(graph[i])[0]))

            for leaf, newLeaf in leafs:
                graph[newLeaf].remove(leaf)
                    
        return ans