class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return self.quickSelect(points, 0, len(points) - 1, k)
        
    
    def quickSelect(self, points, i, j, k):
        
        index = self.partition(points, i, j)
        if index == k - 1:
            return points[:k]
        
        if index < k - 1:
            return self.quickSelect(points, index + 1, j, k)
        else:
            return self.quickSelect(points, i, index - 1, k)
        
        
    def partition(self, points, i, j):
        pivotIndex = random.randrange(i, j + 1)
        pivot = points[pivotIndex]
        points[pivotIndex], points[j] = points[j], points[pivotIndex]
        
        left = i
        for index in range(i, j):
            if self.distance(points[index]) < self.distance(points[j]):
                points[index], points[left] = points[left], points[index]
                left += 1
        for index in range(left, j):
            if self.distance(points[index]) == self.distance(points[j]):
                points[index], points[left] = points[left], points[index]
                left += 1
        points[left], points[j] = points[j], points[left]
        
        return left
        
    
    def distance(self, point):
        return point[0] ** 2 + point[1] ** 2
        