class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(set)
        parent = collections.defaultdict(int)
        for nextNode, node in prerequisites:
            graph[node].add(nextNode)
            parent[nextNode] += 1
       
        
        que = collections.deque()
        for node in range(numCourses):
            if parent[node] == 0:
                que.appendleft(node)
        
        
        ans = []
        total_edge = len(prerequisites)
        
        while que:
            node = que.pop()
            ans.append(node)
            
            for nextNode in graph[node]:
                total_edge -= 1
                parent[nextNode] -= 1
                if parent[nextNode] == 0:
                    que.appendleft(nextNode)
                    
        return ans if total_edge == 0 else []