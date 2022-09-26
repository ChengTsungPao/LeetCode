class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = collections.defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
            
        for key in graph.keys():
            graph[key].sort()
        
        n = len(tickets)
        
        ans = ["JFK"]
        def recur(start):
            if len(ans) == n + 1:
                return True
            
            for i, end in enumerate(graph[start]):
                if graph[start][i] == "#":
                    continue

                graph[start][i] = "#"
                ans.append(end)
                
                if recur(end):
                    return True
                
                graph[start][i] = end
                ans.pop()
                
            return False
        
        recur("JFK")
        
        return ans