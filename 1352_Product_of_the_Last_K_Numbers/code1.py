class ProductOfNumbers:

    def __init__(self):
        self.product = [1]
        
    def add(self, num: int) -> None:
        if num > 0:
            self.product.append(self.product[-1] * num)
        else:
            self.product = [1]
        
    def getProduct(self, k: int) -> int:
        index = len(self.product) - k - 1
        if index < 0:
            return 0
        else:
            return self.product[-1] // self.product[index]
        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)