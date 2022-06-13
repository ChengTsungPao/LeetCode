class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        
        color = collections.defaultdict(int)
        colorBitmap = collections.defaultdict(int)
        
        graph = collections.defaultdict(list)
        for node1, node2 in paths:
            graph[node1].append(node2)
            graph[node2].append(node1)

        def recur(node):
            if color[node] > 0:
                return True
            
            for i in range(4):
                if (colorBitmap[node] >> i) & 1:
                    continue
                
                mark = set()
                color[node] = i + 1
                for nextNode in graph[node]:
                    if not (colorBitmap[nextNode] >> i) & 1:
                        mark.add(nextNode)
                        colorBitmap[nextNode] += 2 ** i
                    
                if all([recur(nextNode) for nextNode in graph[node]]):
                    return True
                
                color[node] = 0
                for nextNode in mark:
                    colorBitmap[nextNode] -= 2 ** i
            
            return False
        
        for node in range(1, n + 1):
            recur(node)
            
        ans = []
        for node in range(1, n + 1):
            ans.append(color[node])
            
        return ans