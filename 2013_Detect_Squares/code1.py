class DetectSquares:

    def __init__(self):
        self.x_set = collections.defaultdict(set)
        self.y_set = collections.defaultdict(set)
        self.countPoint =  collections.defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.x_set[x].add(y)
        self.y_set[y].add(x)
        self.countPoint[x, y] += 1

    def count(self, point: List[int]) -> int:
        square = 0
        x, y = point
        for y_ in self.x_set[x]:
            d = abs(y - y_)
            if d != 0 and x + d in self.y_set[y] and x + d in self.y_set[y_]:
                square += self.countPoint[x, y_] * self.countPoint[x + d, y] * self.countPoint[x + d, y_]
            if d != 0 and x - d in self.y_set[y] and x - d in self.y_set[y_]:
                square += self.countPoint[x, y_] * self.countPoint[x - d, y] * self.countPoint[x - d, y_]
        return square

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)