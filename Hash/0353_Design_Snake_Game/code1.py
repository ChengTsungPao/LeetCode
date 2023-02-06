class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        
        self.orderedDict = collections.OrderedDict([((0, 0), True)])
        self.score = 0
        
        self.position = (0, 0)
        self.speed = {"R": (0, 1), "D": (1, 0), "L": (0, -1), "U": (-1, 0)}
        
    def move(self, direction: str) -> int:
        i, j = self.position
        di, dj = self.speed[direction]
        i, j = i + di, j + dj
        
        # snake hit wall
        if not (0 <= i < self.height and 0 <= j < self.width): 
            return -1
        
        # snake move or eat food
        if self.score >= len(self.food) or self.food[self.score] != [i, j]: 
            self.orderedDict.popitem(last = False)
        else:
            self.score += 1
        
        # snake hit body
        if (i, j) in self.orderedDict: 
            return -1
        
        self.orderedDict[i, j] = True
        self.position = (i, j)
        return self.score
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)