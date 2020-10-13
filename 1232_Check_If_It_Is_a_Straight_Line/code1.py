class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2 : return True
        dx, dy = coordinates[0][0] - coordinates[1][0], coordinates[0][1] - coordinates[1][1]
        for i in range(2, len(coordinates)):
            if dx * (coordinates[i][1] - coordinates[i - 1][1]) != dy * (coordinates[i][0] - coordinates[i - 1][0]):
                return False
        return True