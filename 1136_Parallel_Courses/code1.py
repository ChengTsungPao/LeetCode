class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        parent = collections.defaultdict(int)
        for node, nextNode in relations:
            graph[node].append(nextNode)
            parent[nextNode] += 1
            
        total_edge = len(relations)
        
        stack = []
        for node in range(n):
            if parent[node] == 0:
                stack.append(node)
        
        ans = 0
        while stack:
            
            newStack = []
            while stack:
                node = stack.pop()
                
                for nextNode in graph[node]:
                    if parent[nextNode] == 0:
                        continue
                    
                    total_edge -= 1
                    parent[nextNode] -= 1
                    if parent[nextNode] == 0:
                        newStack.append(nextNode)
                        
            stack = newStack
            ans += 1
                
        return ans if total_edge == 0 else -1