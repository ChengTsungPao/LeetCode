# time: O(m * n)
# space: O(m + n)

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
        
        queK = {}
        que = set()
        
        que.add((0, 0))
        queK[0, 0] = k
        
        step = 0
        
        while que:
            queTemp = set()

            while que:
                x, y = que.pop()
                k = queK[x, y]

                if x == m - 1 and y == n - 1:
                    return step

                for _x, _y in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                    if not (0 <= _x < m and 0 <= _y < n):
                        continue

                    _k = k - (grid[_x][_y] == 1)

                    if queK.get((_x, _y), -1) >= _k or _k < 0:
                        continue

                    queK[_x, _y] = _k
                    queTemp.add((_x, _y))
                    
            que = queTemp
            step += 1
                
        return -1
        