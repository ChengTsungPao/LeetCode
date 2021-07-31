class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        
        def calculateAngle(vector):
            return math.atan2(vector[1], vector[0]) / math.pi * 180
        
        # 計算角度，並記錄相同點數量
        same_point = 0
        angle_sort = []
        for i in range(len(points)):
            vector = [points[i][0] - location[0], points[i][1] - location[1]]
            if vector == [0, 0]:
                same_point += 1
            else:
                angle_sort.append(calculateAngle(vector))
                
        # 將angle_sort重複加入(同界角)，因為角度可循環
        length = len(angle_sort)
        angle_sort.sort()
        for i in range(length):
            angle_sort.append(angle_sort[i] + 360)
        
        # 計算可視範圍的數量
        ans, i, j = 0, 0, 0
        while i < length:
            while angle_sort[j] - angle_sort[i] <= angle and j - length < i:
                j += 1
            j -= 1
            ans = max(ans, j - i + 1)
            i += 1
            
        return ans + same_point
