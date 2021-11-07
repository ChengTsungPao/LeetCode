class MedianFinder:

    def __init__(self):
        self.array = []
        
        
    def addNum(self, num: int) -> None:
        self.array.insert(bisect.bisect_left(self.array, num), num)
        
        
    def findMedian(self) -> float:
        n = len(self.array)
        if n % 2:
            return self.array[n // 2]
        else:
            return (self.array[n // 2] + self.array[n // 2 - 1]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()