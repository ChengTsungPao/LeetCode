class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.bit = 2 ** len(characters)
        self.characters = characters
        self.combinationLength = combinationLength
        self.updateBit()
        
    def updateBit(self):
        self.bit -= 1
        while bin(self.bit).count("1") != self.combinationLength:
            self.bit -= 1
        
    def next(self) -> str:
        str_ = ""
        for ch, b in zip(self.characters, bin(self.bit)[2:].zfill(len(self.characters))):
            if b == "1":
                str_ += ch
                
        self.updateBit()
        return str_

    def hasNext(self) -> bool:
        return self.bit > 0
        

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()