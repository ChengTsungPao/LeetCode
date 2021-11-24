class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        
        self.k = 2
        
        self.vector = [v1, v2]
        self.vectorIndex = [0] * self.k
        self.index = 0
        
        self.count = 0
        for vector in self.vector:
            self.count += len(vector)

        
    def next(self) -> int:
        start = self.index % self.k
        end = start + self.k
        
        for reminder in range(start, end):
            reminder = reminder % self.k
            index = self.vectorIndex[reminder]
                
            if index == len(self.vector[reminder]):
                continue
                
            element = self.vector[reminder][index]
            self.vectorIndex[reminder] += 1
            self.index += 1

            return element
            
            
    def hasNext(self) -> bool:
        return self.count != sum(self.vectorIndex)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())