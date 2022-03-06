class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == [0, 0] and p2 == [0, 0] and p3 == [0, 0] and p4 == [0, 0]:
            return False
        
        def sub(point1, point2):
            return point1[0] - point2[0], point1[1] - point2[1]
        
        def middlePoint(point1, point2):
            return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2
        
        def magnitude(vector):
            return vector[0] ** 2 + vector[1] ** 2
        
        def dot(vector1, vector2):
            return vector1[0] * vector2[0] + vector1[1] * vector2[1]
        
        p = [p1, p2, p3, p4]
        
        for i in range(4):
            for j in range(i + 1, 4):
                candidate = set([0, 1, 2, 3])
                candidate -= set([i, j])

                p1 = p[i]
                p2 = p[j]
                p3 = p[candidate.pop()]
                p4 = p[candidate.pop()]
                vector1 = sub(p1, p2)
                vector2 = sub(p3, p4)
                
                if middlePoint(p1, p2) != middlePoint(p3, p4) or magnitude(vector1) != magnitude(vector2) or dot(vector1, vector2) != 0:
                    continue
   
                return True
            
        return False