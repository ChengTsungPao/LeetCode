class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        for node, nextNode in edges:
            graph[node].append(nextNode)
            graph[nextNode].append(node)
        
        
        ans = 0
        def recur(node, preNode, depth):
            nonlocal ans
            
            ret = []
            for nextNode in graph[node]:
                if preNode == nextNode:
                    continue
                ret.append(recur(nextNode, node, depth + 1) + 1)
            ret.sort(reverse = True)
            
            ans = max(ans, sum(sorted(ret + [depth], reverse = True)[:2]))
            return max(ret, default = 0)
        
        recur(0, -1, 0)
        return ans