class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.checkout = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        try:
            self.checkin[stationName][id] = t
        except:
            try:
                self.checkin[stationName].update({id : t})
            except:
                self.checkin.update({stationName : {id : t}})

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        try:
            self.checkout[stationName][id] = t
        except:
            try:
                self.checkout[stationName].update({id : t})
            except:
                self.checkout.update({stationName : {id : t}})

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        s = 0
        cnt = 0
        for k in self.checkin[startStation].keys():
            try:
                s += (self.checkout[endStation][k] - self.checkin[startStation][k]) 
                cnt += 1
            except:
                pass
        return s/cnt
            
            
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
