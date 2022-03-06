class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        
        self.head = (0, 0)
        self.snack = collections.OrderedDict([((0, 0), True)])
        self.action = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        self.food = food
        self.length = 0

    def move(self, direction: str) -> int:
        di, dj = self.action[direction]
        
        i, j = self.head
        i, j = i + di, j + dj
        
        if not (0 <= i < self.height and 0 <= j < self.width):
            return -1
        
        if self.length < len(self.food) and self.food[self.length] == [i, j]:
            self.length += 1
        else:
            self.snack.popitem(last = False)
            
        if (i, j) in self.snack:
            return -1
            
        self.snack[i, j] = True
        self.head = (i, j)
        
        return self.length


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)