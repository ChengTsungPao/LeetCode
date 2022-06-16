class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        group = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                target = word[:i] + "#" + word[i + 1:]
                group[target].add(word)
                
                
        que = collections.deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while que:
            word, step = que.pop()
            
            if word == endWord:
                return step
            
            for i in range(len(word)):
                target = word[:i] + "#" + word[i + 1:]
                for nextWord in group[target]:
                    if nextWord in visited:
                        continue
                        
                    visited.add(nextWord)
                    que.appendleft((nextWord, step + 1))
                    
                del group[target]
                    
        return 0