class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        
        '''
        Bellman Ford => "check negative edge" just find the distance array update or not at final loop
        '''                    
        
        probability = [0] * n
        probability[start] = 1
        
        for _ in range(n - 1):
            preProbability = probability.copy()
            
            for (u, v), prob in zip(edges, succProb):
                if preProbability[u] != 0:
                    probability[v] = max(probability[v], preProbability[u] * prob)
                    
                if preProbability[v] != 0:
                    probability[u] = max(probability[u], preProbability[v] * prob)
                    
        return probability[end] if probability[end] != 0 else 0