class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        def findTwoMax(arr):
            if len(arr) <= 2:
                return arr
            
            ans = []
            for num in arr:
                if len(ans) < 2:
                    ans.append(num)
                elif ans[0] < num:
                    ans[0] = num
                
                if len(ans) >= 2 and ans[0] > ans[1]:
                    ans[0], ans[1] = ans[1], ans[0]
                    
            return ans
        
        
        graph = collections.defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        
        ans = -float("inf")
        visited = set()
        def dfs(node, height):
            nonlocal ans
            
            ret = []
            for nextNode in graph[node]:
                if nextNode in visited:
                    continue
                    
                visited.add(nextNode)
                ret.append(dfs(nextNode, height + 1) + 1)
                visited.remove(nextNode)
   
            ans = max(ans, sum(findTwoMax(ret + [height])))
            return 0 if ret == [] else max(ret)
        
        visited.add(0)
        dfs(0, 0)
        visited.remove(0)
        
        return ans