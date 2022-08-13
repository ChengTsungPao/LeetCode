class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        n = len(grades)
        
        def solve(n):
            # x * (x + 1) / 2 = n
            return int((-1 + (1 + 8 * n) ** 0.5) / 2)
        
        return solve(n)