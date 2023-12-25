class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        
        count = collections.Counter()
        for g in grid:
            count += collections.Counter(g)
        
        ans = [-1, -1]
        for i in range(1, n * n + 1):
            if count[i] == 0:
                ans[1] = i
            elif count[i] == 2:
                ans[0] = i
                
        return ans