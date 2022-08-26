class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        n = len(wordList)
        
        def isConnect(word1, word2):
            count = 0
            for ch1, ch2 in zip(word1, word2):
                count += ch1 != ch2
            return count == 1
        
        graph = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                word1, word2 = wordList[i], wordList[j]
                if isConnect(word1, word2):
                    graph[word1].append(word2)
                    graph[word2].append(word1)
        
        if beginWord not in wordList:
            for word in wordList:
                if isConnect(beginWord, word):
                    graph[beginWord].append(word)
                    graph[word].append(beginWord)
                    
        ans = []
        stack = [(beginWord, [beginWord])]
        visited = set([beginWord])
        
        while stack and not ans:

            nextStack = []
            newVisited = set()
            for word, path in stack:
                if word == endWord:
                    ans.append(path)
                    
                for nextWord in graph[word]:
                    if nextWord in visited:
                        continue
                    newVisited.add(nextWord)
                        
                    nextStack.append((nextWord, path + [nextWord]))
            
            visited |= newVisited
            stack = nextStack
            
        return ans