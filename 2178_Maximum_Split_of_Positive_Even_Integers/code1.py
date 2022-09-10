class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        
        if finalSum % 2:
            return []
        
        def solve(s):
            # n * (n + 1) = s
            return int((-1 + (1 + 4 * s) ** 0.5) / 2)
        
        n = solve(finalSum)
        addNum = finalSum - n * (n + 1)
        
        ans = list(range(2, 2 * n + 1, 2))
        ans[-1] += addNum
        
        return ans