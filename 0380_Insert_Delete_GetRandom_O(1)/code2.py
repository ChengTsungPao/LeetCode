class RandomizedSet:

    def __init__(self):
        self.valIndex = {}
        self.val = []

    def insert(self, val: int) -> bool:
        if val in self.valIndex:
            return False
        else:
            self.valIndex[val] = len(self.val)
            self.val.append(val)
            return True
        
    def remove(self, val: int) -> bool:
        if val not in self.valIndex:
            return False
        else:
            index = self.valIndex[val]
            self.val[-1], self.val[index] = self.val[index], self.val[-1]
            self.valIndex[self.val[index]] = index
            self.val.pop()
            del self.valIndex[val]
            return True        

    def getRandom(self) -> int:
        return self.val[random.randrange(0, len(self.val))]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()