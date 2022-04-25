class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        n = len(parent)
        
        graph = collections.defaultdict(list)
        for i in range(1, n):
            graph[parent[i]].append(i)
            
        
        ans = 1
        def recur(node):
            nonlocal ans
            
            if len(graph[node]) == 0:
                return 1, s[node]
            
            height1 = height2 = 0
            for nextNode in graph[node]:
                height, ch = recur(nextNode)
                if ch != s[node]:
                    height1 = max(height1, height)
                    height1, height2 = sorted([height1, height2])
            
            ans = max(ans, height1 + height2 + 1)
            return max(height1, height2) + 1, s[node]
            
        recur(0)
        return ans