class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        
        n = len(s)
        
        def findWord(word):
            ret = []
            length = len(word)
            for i in range(n):
                i, j = i, i + length
                if s[i: j] == word:
                    ret.append((i, j))
            return ret
        
        record = [False] * n
        for word in words:
            for i, j in findWord(word):
                for index in range(i, j):
                    record[index] = True
        
        isWord = False
        for index in range(n - 1, -1, -1):
            if not isWord and record[index]:
                isWord = True
                s = s[:index + 1] + "</b>" + s[index + 1:]
            elif isWord and record[index]:
                continue
            elif isWord and not record[index]:
                isWord = False
                s = s[:index + 1] + "<b>" + s[index + 1:]
                
        if isWord:
            s = "<b>" + s
                
        return s