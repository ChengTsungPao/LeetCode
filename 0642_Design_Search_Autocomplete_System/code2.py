class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.countWord = collections.defaultdict(int)
        for sentence, time in zip(sentences, times):
            self.countWord[sentence] += time
        self.currentWord = ""
        self.currentSentence = [sentence for sentence, time in sorted(self.countWord.items(), key = lambda x: (-x[1], x[0]))]
        self.currentCompareIndex = 0
            
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.countWord[self.currentWord] += 1
            self.currentWord = ""
            self.currentSentence = [sentence for sentence, time in sorted(self.countWord.items(), key = lambda x: (-x[1], x[0]))]
            self.currentCompareIndex = 0
            return []
        
        currentSentenceHit = []
        for sentence in self.currentSentence:
            if self.currentCompareIndex < len(sentence) and sentence[self.currentCompareIndex] == c:
                currentSentenceHit.append(sentence)
        self.currentSentence = currentSentenceHit
        
        self.currentWord += c
        self.currentCompareIndex += 1
        
        return self.currentSentence[:3]