class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        
        city_len = len(flights)
        week_len = len(days[0])
        
        graph = collections.defaultdict(list)
        for cityi in range(city_len):
            for cityj in range(city_len):
                if flights[cityi][cityj] or cityi == cityj:
                    graph[cityi].append(cityj)
        
        memo = {}
        def recur(city, week):
            
            if (city, week) not in memo:
            
                if week >= week_len:
                    return 0

                ans = 0
                for nextCity in graph[city]:
                    ans = max(ans, days[nextCity][week] + recur(nextCity, week + 1))
                    
                memo[city, week] = ans
                
            return memo[city, week]
        
        return recur(0, 0)