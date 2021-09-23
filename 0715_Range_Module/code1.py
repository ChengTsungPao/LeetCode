class RangeModule:

    def __init__(self):
        self.data = []
        
    def findIndex(self, left: int, right: int):
        return bisect.bisect_left(self.data, left), bisect.bisect_right(self.data, right)
        
    def addRange(self, left: int, right: int) -> None:
        left_index, right_index = self.findIndex(left, right)
        if left_index % 2 == 0 and right_index % 2 == 0:
            self.data = self.data[:left_index] + [left, right] + self.data[right_index:]
        elif left_index % 2 == 0 and right_index % 2 == 1:
            self.data = self.data[:left_index] + [left] + self.data[right_index:]
        elif left_index % 2 == 1 and right_index % 2 == 0:
            self.data = self.data[:left_index] + [right] + self.data[right_index:]
        else:
            self.data = self.data[:left_index] + self.data[right_index:]
        
    def queryRange(self, left: int, right: int) -> bool:
        left_index, right_index = self.findIndex(left, right)
        if left_index == right_index:
            return left_index % 2 == 1
        elif left_index % 2 == 0:
            return self.data[left_index] <= left and self.data[left_index + 1] >= right
        else:
            return self.data[left_index - 1] <= left and self.data[left_index] >= right
        
    def removeRange(self, left: int, right: int) -> None:
        left_index, right_index = self.findIndex(left, right)
        if left_index % 2 == 0 and right_index % 2 == 0:
            self.data = self.data[:left_index] + self.data[right_index:]
        elif left_index % 2 == 0 and right_index % 2 == 1:
            self.data = self.data[:left_index] + [right] + self.data[right_index:]
        elif left_index % 2 == 1 and right_index % 2 == 0:
            self.data = self.data[:left_index] + [left] + self.data[right_index:]
        else:
            self.data = self.data[:left_index] + [left, right] + self.data[right_index:]

            
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)