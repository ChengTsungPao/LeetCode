class RandomizedSet:

    def __init__(self):
        self.data = set()

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        else:
            self.data.add(val)
            return True       

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.remove(val)
            return True
        else:
            return False 
        
    def getRandom(self) -> int:
        return list(self.data)[random.randint(0, len(self.data) - 1)]
