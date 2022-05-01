class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        child = [0] * n
        reverseGraph = collections.defaultdict(list)
        
        for node in range(n):
            for nextNode in graph[node]:
                child[node] += 1
                reverseGraph[nextNode].append(node)
        
        que = collections.deque()
        for node in range(n):
            if child[node] == 0:
                que.appendleft(node)
        
        ans = []

        while que:
            node = que.pop()
            ans.append(node)
            
            for nextNode in reverseGraph[node]:
                if child[nextNode] == 0:
                    continue
                    
                child[nextNode] -= 1
                if child[nextNode] == 0:
                    que.appendleft(nextNode)
                    
        return sorted(ans)