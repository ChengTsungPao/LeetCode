class RandomizedSet:

    def __init__(self):
        self.valIndex = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.valIndex:
            return False
        
        index = len(self.vals)
        self.valIndex[val] = index
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valIndex:
            return False
        
        index, lastVal = self.valIndex[val], self.vals[-1]
        self.valIndex[lastVal] = index
        self.vals[index], self.vals[-1] = self.vals[-1], self.vals[index]
        
        del self.valIndex[val]
        self.vals.pop()
        return True
        
    def getRandom(self) -> int:
        return self.vals[random.randrange(0, len(self.vals))]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()