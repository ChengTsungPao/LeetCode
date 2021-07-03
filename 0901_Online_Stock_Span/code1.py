class StockSpanner:

    def __init__(self):
        self.record = ()
        
    def next(self, price: int) -> int:
        ans = 1
        index = len(self.record) - 1
        while index >= 0:
            if self.record[index][0] <= price:
                ans += self.record[index][1]
                index -= self.record[index][1]
            else:
                break
        self.record += (price, ans),
        return ans

        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)