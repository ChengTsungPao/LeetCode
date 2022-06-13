class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        for node1, node2 in paths:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        ans = [0] * n
        for node in range(1, n + 1):
            candidate = set([1, 2, 3, 4]) - set([ans[nextNode - 1] for nextNode in graph[node]])     
            ans[node - 1] = candidate.pop()
                    
        return ans