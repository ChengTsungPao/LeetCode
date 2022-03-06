class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.stack = [num for num in range(maxNumbers)]
        self.cache = set()
        
    def get(self) -> int:
        if not self.stack:
            return -1
        
        number = self.stack.pop()
        self.cache.add(number)
        return number

    def check(self, number: int) -> bool:
        return number not in self.cache
        
    def release(self, number: int) -> None:
        if self.check(number):
            return
        
        self.cache.remove(number)
        self.stack.append(number)
        

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)