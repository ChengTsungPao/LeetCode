class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        graph = collections.defaultdict(list)
        for nextNode, node in richer:
            graph[node].append(nextNode)
        
        @functools.lru_cache(None)
        def recur(node):
            if not graph[node]:
                return node
            return min([node] + [recur(nextNode) for nextNode in graph[node]], key = lambda x: quiet[x])
        
        return [recur(node) for node in range(len(quiet))]