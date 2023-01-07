class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        
        n = len(stones)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
            
        @functools.lru_cache(None)
        def recur(i, j, num_of_split):
            
            num_of_stone = j - i + 1
            if (num_of_stone - num_of_split) % (k - 1):
                return float("inf")
            elif num_of_stone == 1:
                return 0 if num_of_split == 1 else float("inf")
            elif num_of_split == 1:
                return recur(i, j, k) + (preSum[j + 1] - preSum[i])
                
            return min([recur(i, m, 1) + recur(m + 1, j, num_of_split - 1) for m in range(i, j)])
        
        ans = recur(0, n - 1, 1)
        return ans if ans != float("inf") else -1