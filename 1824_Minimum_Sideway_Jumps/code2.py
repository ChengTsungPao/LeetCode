class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        
        # 若current收集到0, 1, 2, 3代表已經是下一次的最佳決策
        
        for start in range(len(obstacles)):
            if obstacles[start] == 2:
                break
                
        if start == len(obstacles) - 1:
            count = 0
        else:
            count = 1
        
        current = set([0, obstacles[start - 1], obstacles[start]])
        for index in range(start + 1, len(obstacles)):
            current.add(obstacles[index])
            if current == {0, 1, 2, 3}:
                count += 1
                current = set([0, obstacles[index - 1], obstacles[index]])

        return count
