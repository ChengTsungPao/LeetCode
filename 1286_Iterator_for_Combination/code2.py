class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.index = 0
        self.length = math.comb(len(characters), combinationLength)
        self.combinationFcn = self.combination(characters, combinationLength)
        
    def combination(self, characters, combinationLength):
        if combinationLength == 0:
            yield ""
            return None

        for i in range(len(characters) - combinationLength + 1):
            for word in self.combination(characters[i + 1:], combinationLength - 1):
                yield characters[i] + word
                
        return None
    
    def next(self) -> str:
        self.index += 1
        return next(self.combinationFcn)

    def hasNext(self) -> bool:
        return self.index < self.length
        

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()