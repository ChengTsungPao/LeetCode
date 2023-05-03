class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        ans = 0
        visited = set([0])
        def recur(node):
            nonlocal ans
            
            updateCache = collections.defaultdict(int)
            
            status = []
            for nextNode in graph[node]:
                if nextNode in visited:
                    continue
                    
                visited.add(nextNode)
                status.append(recur(nextNode))
                visited.remove(nextNode)
            
            # 計算目前Node
            value = vals[node]
            for cache in status:
                ans += cache.get(value, 0)
            
            # 把目前的Node更新再child的cache
            for cache in status:
                for value in list(cache.keys()):
                    if vals[node] > value:
                        del cache[value]
            updateCache[vals[node]] += 1
                        
            # 配對目前node之外的數值
            for i in range(len(status)):
                for j in range(i + 1, len(status)):
                    if len(status[i]) > len(status[j]):
                        a, b = j, i
                    else:
                        a, b = i, j
                    for valuei in status[a].keys():
                        if valuei in status[b]:
                            ans += status[a][valuei] * status[b][valuei]

            # update "updateCache"             
            for i in range(len(status)):
                for value in status[i].keys():
                    updateCache[value] += status[i][value]
                    
            return updateCache
        
        recur(0)
        return ans + len(edges) + 1