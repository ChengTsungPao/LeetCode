class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        
        n = len(obstacles)
        
        que = collections.deque([(1, 0, 0)])
        cache = set([(1, 0)])
        
        while que:
            i, j, step = que.popleft()
            
            if j == n - 1:
                return step
            
            for k, (i_, j_) in enumerate([(i, j + 1), (i + 1, j), (i + 2, j), (i - 1, j), (i - 2, j)]):
                if not (0 <= i_ <= 2) or obstacles[j_] == i_ + 1 or (i_, j_) in cache:
                    continue
                    
                que.append((i_, j_, step if k == 0 else step + 1))
                cache.add((i_, j_))
        
        return -1