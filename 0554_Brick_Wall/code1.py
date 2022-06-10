class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        n = len(wall)
        
        count = collections.defaultdict(int)
        for i in range(n):
            width = 0
            for j in range(len(wall[i]) - 1):
                width += wall[i][j]
                count[width] += 1
                
        return n - max(count.values(), default = 0)