class StreamChecker:
    def __init__(self, words: List[str]):    
        self.trie = {}
        for word in words:
            pointer = self.trie
            for ch in word[::-1]:
                if ch not in pointer:
                    pointer[ch] = {"isWord": False}
                pointer = pointer[ch]
            pointer["isWord"] = True
        self.curWord = ""
        
    def query(self, letter: str) -> bool:
        self.curWord = letter + self.curWord
        pointer = self.trie
        for ch in self.curWord:
            if ch not in pointer:
                return False
            pointer = pointer[ch]
            if pointer["isWord"]:
                return True
        return pointer["isWord"]
        
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)