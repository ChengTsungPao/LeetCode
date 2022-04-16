class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        isValid = set()
        graph = collections.defaultdict(list)
        for node, nextNode in connections:
            graph[node].append(nextNode)
            graph[nextNode].append(node)
            isValid.add((nextNode, node))
            
        
        ans = 0
        isVisited = set([0])
        que = collections.deque([0])
        while que:
            node = que.pop()
            
            for preNode in graph[node]:
                if preNode in isVisited:
                    continue
                    
                if (node, preNode) not in isValid:
                    ans += 1
                isVisited.add(preNode)
                que.appendleft(preNode)
                
        return ans