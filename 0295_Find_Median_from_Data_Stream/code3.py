from sortedcontainers import SortedList

class MedianFinder:

    def __init__(self):
        self.bst = SortedList()

    def addNum(self, num: int) -> None:
        self.bst.add(num)

    def findMedian(self) -> float:
        length = len(self.bst)
        return (self.bst[length // 2 - (length % 2 == 0)] + self.bst[length // 2]) / 2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()