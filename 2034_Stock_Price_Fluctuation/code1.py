from sortedcontainers import SortedList

class StockPrice:

    def __init__(self):
        self.bst = SortedList()
        self.prices = {}
        self.curTime = -1
        
    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.prices:
            self.bst.remove((self.prices[timestamp], timestamp))
        self.bst.add((price, timestamp))
        self.prices[timestamp] = price
        self.curTime = max(self.curTime, timestamp)

    def current(self) -> int:
        return self.prices[self.curTime]

    def maximum(self) -> int:
        return self.bst[-1][0]
        
    def minimum(self) -> int:
        return self.bst[0][0]
        

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()