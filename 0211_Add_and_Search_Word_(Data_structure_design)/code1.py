class WordDictionary:

    def __init__(self):
        self.data = " "        

    def addWord(self, word: str) -> None:
        self.data += word + " "        

    def search(self, word: str) -> bool:
        import re
        if(re.search(" " + word.replace(".","[a-zA-Z]") + " ",self.data)!=None):
            return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)