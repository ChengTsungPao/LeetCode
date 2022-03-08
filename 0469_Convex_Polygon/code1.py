class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        
        def sub(point1, point2):
            return point1[0] - point2[0], point1[1] - point2[1]
        
        def getAngle(vector1, vector2):
            operation = complex(vector2[0], vector2[1]) / complex(vector1[0], vector1[1])
            return math.atan2(operation.imag, operation.real) * 180 / math.pi
        
        points = points[::-1]
        points = [points[-1]] + points + [points[0]]
        
        preAngle = 0
        for i in range(1, len(points) - 1):
            vector1 = sub(points[i - 1], points[i])
            vector2 = sub(points[i + 1], points[i])
            angle = getAngle(vector1, vector2)

            if preAngle * angle < 0 and abs(int(angle)) != 180:
                return False
            
            if abs(int(angle)) != 180:
                preAngle = angle
            
        return True