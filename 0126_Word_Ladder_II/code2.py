class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        n = len(wordList)
        
        def isConnect(word1, word2):
            count = 0
            for ch1, ch2 in zip(word1, word2):
                count += ch1 != ch2
            return count == 1
        
        # create graph
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
                    
        def getAnswer(stack1, stack2):
            ans = []
            status = collections.defaultdict(list)
            for word2, path2 in stack2:
                status[word2].append(path2)
            
            for word1, path1 in stack1:
                for path2 in status[word1]:
                    ans.append(path1[:-1] + path2[::-1])
            return ans
        
        ans = []
        stack1 = [(beginWord, [beginWord])]
        visited1 = set([beginWord])
        
        stack2 = [(endWord, [endWord])]
        visited2 = set([endWord])
        
        # Bidirectional BFS
        while stack1 and stack2:

            nextStack = []
            newVisited = set()
            for word, path in stack1:
                if word in visited2:
                    return getAnswer(stack1, stack2)
                    
                for nextWord in graph[word]:
                    if nextWord not in visited1:
                        newVisited.add(nextWord)
                        nextStack.append((nextWord, path + [nextWord]))
            
            visited1 |= newVisited
            stack1 = nextStack
            
            nextStack = []
            newVisited = set()
            for word, path in stack2:
                if word in visited1:
                    return getAnswer(stack1, stack2)
                    
                for nextWord in graph[word]:
                    if nextWord not in visited2:
                        newVisited.add(nextWord)
                        nextStack.append((nextWord, path + [nextWord]))
            
            visited2 |= newVisited
            stack2 = nextStack
            
        return []