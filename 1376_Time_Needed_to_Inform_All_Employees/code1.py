class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        # 每個member只有一個manager，所以不會有cycle
        
        def dfs(ID):
            if ID not in graph:
                return 0
            
            ans = 0
            for next_id in graph[ID]:
                ans = max(ans, dfs(next_id) + informTime[next_id])
                
            return ans
        
        
        graph = collections.defaultdict(list)
        
        for i in range(len(manager)):
            graph[manager[i]].append(i)

        return dfs(-1)