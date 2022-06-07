class UndergroundSystem:

    def __init__(self):
        self.currentOrder = collections.defaultdict(lambda: (0, 0))
        self.averageTime  = collections.defaultdict(lambda: (0, 0))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.currentOrder[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.currentOrder[id]
        del self.currentOrder[id]
        averageTime, times = self.averageTime[startStation, stationName]
        averageTime = (averageTime * times + (t - startTime)) / (times + 1)
        self.averageTime[startStation, stationName] = (averageTime, times + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.averageTime[startStation, endStation][0]
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)