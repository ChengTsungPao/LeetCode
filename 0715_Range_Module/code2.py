class RangeModule:

    def __init__(self):
        self.sortedArr = []
        
    def findIndex(self, left: int, right: int) -> List[int]:
        return bisect.bisect_left(self.sortedArr, left), bisect.bisect_right(self.sortedArr, right)
        
    def addRange(self, left: int, right: int) -> None:
        leftIndex, rightIndex  = self.findIndex(left, right)
        if leftIndex % 2 and rightIndex % 2:
            self.sortedArr[leftIndex: rightIndex] = []
        elif leftIndex % 2:
            self.sortedArr[leftIndex: rightIndex] = [right]
        elif rightIndex % 2:
            self.sortedArr[leftIndex: rightIndex] = [left]
        else:
            self.sortedArr[leftIndex: rightIndex] = [left, right]
        
    def queryRange(self, left: int, right: int) -> bool:
        leftIndex = bisect.bisect_left(self.sortedArr, left)
        validRange = self.sortedArr[leftIndex: leftIndex + 2] if leftIndex % 2 == 0 else self.sortedArr[leftIndex - 1: leftIndex + 1]
        return len(validRange) == 2 and validRange[0] <= left < right <= validRange[1]

    def removeRange(self, left: int, right: int) -> None:
        leftIndex, rightIndex  = self.findIndex(left, right)
        if leftIndex % 2 and rightIndex % 2:
            self.sortedArr[leftIndex: rightIndex] = [left, right]
        elif leftIndex % 2:
            self.sortedArr[leftIndex: rightIndex] = [left]
        elif rightIndex % 2:
            self.sortedArr[leftIndex: rightIndex] = [right]
        else:
            self.sortedArr[leftIndex: rightIndex] = []        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)