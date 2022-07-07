class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        
        n = len(rectangles)
        C = 10 ** 9
        MOD = C + 7
        
        def rangeOverlapping(range1, range2):
            return max(range1[0], range2[0]), min(range1[1], range2[1])
        
        def rectangleOverlapping(rectangle1, rectangle2):
            x1, y1, x2, y2 = rectangle1
            a1, b1, a2, b2 = rectangle2
            x, a = rangeOverlapping([x1, x2], [a1, a2])
            y, b = rangeOverlapping([y1, y2], [b1, b2])
            if x >= a or y >= b:
                return [0, 0, 0, 0]
            else:
                return [x, y, a, b]            
        
        def area(rectangle):
            return abs(rectangle[0] - rectangle[2]) * abs(rectangle[1] - rectangle[3])
        
        memo = {}
        def recur(index, k):
            
            if (index, k) not in memo:

                if k == 0:
                    return [[0, 0, C, C]]
                elif index >= n:
                    return []

                ans = []
                for i in range(index, n):
                    rectanglei = rectangles[i]
                    for rectanglej in recur(i + 1, k - 1):
                        rectangle = rectangleOverlapping(rectanglei, rectanglej)
                        if area(rectangle) == 0:
                            continue
                        ans.append(rectangle)
                        
                memo[index, k] = ans
                    
            return memo[index, k]
        
        ans = 0
        for k in range(1, n + 1):
            sum_ = 0
            for rectangle in recur(0, k):
                sum_ += area(rectangle)
                
            if sum_ == 0:
                break
                
            ans += sum_ if k % 2 == 1 else -sum_
            ans %= MOD
            
        return ans