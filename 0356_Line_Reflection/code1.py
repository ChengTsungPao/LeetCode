class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        
        def findMedian(xPoints):
            n = len(xPoints)
            xPoints = sorted(xPoints)
            if n % 2:
                return xPoints[n // 2]
            else:
                return (xPoints[n // 2] + xPoints[n // 2 - 1]) / 2
                
        def isValid(xPoints, center):
            for xPoint in xPoints:
                if 2 * center - xPoint not in xPoints:
                    return False
            return True
        
        count = collections.defaultdict(set)
        for x, y in points:
            count[y].add(x)

        center = findMedian(list(count.values())[0])
        for xPoints in count.values():
            if center != findMedian(xPoints):
                return False
            if isValid(xPoints, center) == False:
                return False
        
        return True