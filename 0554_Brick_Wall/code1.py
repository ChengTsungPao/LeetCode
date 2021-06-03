class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        count = collections.defaultdict(int)
        count[0] = 0
        
        for i in range(len(wall)):
            s = wall[i][0]
            for j in range(1, len(wall[i])):
                count[s] += 1
                s += wall[i][j]

        return len(wall) - max(count.values())