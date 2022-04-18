class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.arr = vec
        self.row = 0
        self.col = 0
        
    def check(self):
        while self.row < len(self.arr) and len(self.arr[self.row]) == 0:
            self.row += 1
        
    def next(self) -> int:
        self.check()
        value = self.arr[self.row][self.col]
        if self.col == len(self.arr[self.row]) - 1:
            self.row += 1
            self.col = 0
        else:
            self.col += 1
        return value
        
    def hasNext(self) -> bool:
        self.check()
        return self.row < len(self.arr)
        
        
# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()