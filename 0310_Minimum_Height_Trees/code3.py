class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        connect = collections.defaultdict(int)
        graph = collections.defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
            connect[node1] += 1
            connect[node2] += 1
            
        stack = []
        visited = set()
        for node in range(n):
            if connect[node] == 1:
                stack.append(node)
                
        ans = [0] * n 
        while stack:
            
            ans = stack.copy()
            newStack = []
            for node in stack:                
                visited.add(node)
                
                for nextNode in graph[node]:
                    if nextNode in visited:
                        continue
                        
                    connect[nextNode] -= 1
                    if connect[nextNode] == 1:
                        newStack.append(nextNode)
                        
            stack = newStack.copy()
            
        return ans