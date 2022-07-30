# 阿寶
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        
        ans = []
        
        status = [[] for _ in range(1, 4 + 1)]
        for word in words:
            wordLength = len(word)
            status[wordLength - 1].append(word)
            
        for wordLength in range(1, 4 + 1):
            wordList = status[wordLength - 1]
            if wordList:
                ans.extend(self._wordSquares(wordLength, wordList))
                
        return ans
    
    def _wordSquares(self, wordLength, wordList):
        
        prefixStr = collections.defaultdict(list)
        for word in wordList:
            s = ""
            prefixStr[s].append(word)
            for ch in word:
                s += ch
                prefixStr[s].append(word)

        def check(index, choose, prefixStr):
            wordSet = set()
            for i in range(index, wordLength):
                s = ""
                for j in range(index):
                    s += choose[j][i]
                wordSet.add(s)
            for s in wordSet:
                if len(prefixStr[s]) <= 0:
                    return False
            return True

        def recur(index, choose):
            if index >= wordLength:
                return [[]]

            s = "".join([choose[i][index] for i in range(index)])
            
            ans = []
            for word in prefixStr[s]:
                if check(index + 1, choose + [word], prefixStr):
                    for ret in recur(index + 1, choose + [word]):
                        ans.append([word] + ret)
            return ans
        
        return recur(0, [])