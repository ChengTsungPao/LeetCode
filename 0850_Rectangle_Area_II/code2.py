class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        
        MOD = 10 ** 9 + 7
        
        L = []
        x_set = set()
        for x1, y1, x2, y2 in rectangles:
            x_set.add(x1)            
            x_set.add(x2)
            L.append((y1,  1, x1, x2))
            L.append((y2, -1, x1, x2))
        L.sort()
        all_x = sorted(x_set)
        
        x_i = {x: i for i, x in enumerate(all_x)}
        n = len(x_i)
        
        count = [0] * n
        area = pre_y = cur_x_sum = 0
        for y, target, x1, x2 in L:
            area += (y - pre_y) * cur_x_sum
            for i in range(x_i[x1], x_i[x2]):
                count[i] += target
            
            cur_x_sum = 0
            for i in range(n - 1):
                if count[i] > 0:
                    cur_x_sum += all_x[i + 1] - all_x[i]
                    
            pre_y = y
                    
        return area % MOD