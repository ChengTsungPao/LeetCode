class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0])
        
        prefixSum = copy.deepcopy(grid)
        suffixSum = copy.deepcopy(grid)
        
        for i in range(2):
            for j in range(1, n):
                prefixSum[i][ j] += prefixSum[i][ j - 1]
                suffixSum[i][~j] += suffixSum[i][~j + 1]
        
        # cut1 <= cut2 => prefixSum[0][cut2] - prefixSum[0][cut1]
        # cut1 >= cut2 => suffixSum[1][cut1] - suffixSum[1][cut2]
        
        ans = float("inf")
        for cut1 in range(n):
            maxScore = 0
            for cut2 in range(n):
                if cut1 == cut2:
                    continue

                if cut1 <= cut2:
                    maxScore = max(maxScore, prefixSum[0][cut2] - prefixSum[0][cut1])
                else:
                    maxScore = max(maxScore, suffixSum[1][cut2] - suffixSum[1][cut1])

            ans = min(ans, maxScore)
        
        return ans