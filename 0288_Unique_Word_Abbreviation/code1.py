class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.setup(dictionary)
    
    def setup(self, dictionary: List[str]):
        self.words = set(dictionary)
        self.abbreviation = {}
        for word in self.words:
            abbreviationWord = self.translate(word)
            if abbreviationWord in self.abbreviation:
                self.abbreviation[abbreviationWord] = False
            else:
                self.abbreviation[abbreviationWord] = True
                
    def translate(self, word: str):
        return word[0] + str(len(word) - 2) + word[-1]
        
    def isUnique(self, word: str) -> bool:
        abbreviationWord = self.translate(word)
        
        if word in self.words:
            return self.abbreviation[abbreviationWord]
        
        if abbreviationWord in self.abbreviation:
            return False
        else:
            return True


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)