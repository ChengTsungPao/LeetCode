class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        
        if carpetLen == 1:
            return max(floor.count("1") - numCarpets, 0)
        
        n = len(floor)
        
        suffixSum = [(floor[-1] == "1") * 1] * n
        for i in range(n - 2, -1, -1):
            suffixSum[i] = suffixSum[i + 1] + (floor[i] == "1")
        
        @functools.lru_cache(None)
        def recur(index, numCarpets):
            if index >= n:
                return 0
            elif numCarpets == 0:
                return suffixSum[index]
            
            if floor[index] == "0":
                ans = recur(index + 1, numCarpets)
            else:
                ans = min(recur(index + carpetLen, numCarpets - 1), recur(index + 1, numCarpets) + 1)
            return ans
        
        return recur(0, numCarpets)