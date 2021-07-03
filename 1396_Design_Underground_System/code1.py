class UndergroundSystem:

    def __init__(self):
        self.check = {} # {id : (startStation, t)}
        self.total_time = {} # {(startStation, endStation) : [t, count]}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, endStation = self.check[id][0], stationName
        if (startStation, endStation) not in self.total_time:
            self.total_time[startStation, endStation] = [t - self.check[id][1], 1]
        else:
            self.total_time[startStation, endStation][0] += t - self.check[id][1]
            self.total_time[startStation, endStation][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        t, count = self.total_time[startStation, endStation]
        return t / count
            
        
        
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)