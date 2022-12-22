class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        
        bottom_up_distance = collections.defaultdict(list)
        visited = set()
        def bottom_up(node):
            distance = number_of_node = 0
            
            visited.add(node)
            
            for nextNode in graph[node]:
                if nextNode in visited:
                    continue

                d, number = bottom_up(nextNode)
                distance += d
                bottom_up_distance[node, nextNode] = (d, number)
                number_of_node += number
                
            visited.remove(node)
            
            bottom_up_distance[node, -1] = (distance, number_of_node)
            return distance + number_of_node + 1, number_of_node + 1
        
        ans = [0] * n
        visited = set()
        def top_down(node, distance = 0, number_of_node = 0):
            d, number = bottom_up_distance[node, -1]
            distance += d
            number_of_node += number
            
            ans[node] = distance
            
            visited.add(node)
            
            for nextNode in graph[node]:
                if nextNode in visited:
                    continue
                
                d, number = bottom_up_distance[node, nextNode]
                top_down(nextNode, (distance - d) + (number_of_node - number) + 1, number_of_node - number + 1)
                
            visited.remove(node)
            
        bottom_up(0)
        top_down(0)
        
        return ans