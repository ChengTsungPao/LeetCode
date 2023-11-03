class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        @functools.lru_cache(None)
        def dp(node, preNode, times):
            if times >= 14:
                return 0
            
            opr1 = coins[node] // pow(2, times) - k
            for child in graph[node]:
                if child != preNode:
                    opr1 += dp(child, node, times)
            
            opr2 = coins[node] // pow(2, times + 1)
            for child in graph[node]:
                if child != preNode:
                    opr2 += dp(child, node, times + 1)
            
            return max(opr1, opr2)
        
        return dp(0, -1, 0)