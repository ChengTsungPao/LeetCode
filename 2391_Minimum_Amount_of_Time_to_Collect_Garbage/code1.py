class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        n = len(travel)
        
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + travel[i - 1]
        
        G_count = P_count = M_count = 0
        G_right = P_right = M_right = 0
        
        for i, g in enumerate(garbage):
            count = collections.Counter(g)
            
            if count["G"] > 0: G_right = i
            if count["P"] > 0: P_right = i
            if count["M"] > 0: M_right = i
            
            G_count += count["G"]
            P_count += count["P"]
            M_count += count["M"]

        return preSum[G_right] + G_count + preSum[P_right] + P_count + preSum[M_right] + M_count