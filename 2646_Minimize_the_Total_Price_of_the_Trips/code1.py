class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        nodeVisitedTimes = collections.defaultdict(int)
        def countNodeTimes(node, preNode, end):
            if node == end:
                return True
            for nextNode in graph[node]:
                if nextNode != preNode:
                    nodeVisitedTimes[nextNode] += 1
                    if countNodeTimes(nextNode, node, end):
                        return True
                    nodeVisitedTimes[nextNode] -= 1
            return False
        
        # get node visited times
        for start, end in trips: 
            nodeVisitedTimes[start] += 1
            countNodeTimes(start, -1, end)
        
        # get min cost
        @functools.lru_cache(None)
        def getMinCost(node, preNode, state):
            p, t = price[node], nodeVisitedTimes[node]             
            select = t * p // 2
            noSelect = t * p
            for nextNode in graph[node]:
                if nextNode == preNode:
                    continue
                noSelect += getMinCost(nextNode, node, False)
                if not state: select += getMinCost(nextNode, node, True)
            return min(select, noSelect) if not state else noSelect
        
        return getMinCost(0, -1, False)