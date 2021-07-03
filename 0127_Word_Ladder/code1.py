class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if(endWord not in wordList): 
            return 0              
        
        ans = 0
        check = False
        que = collections.deque()
        que.append((beginWord, 1))
        wordList = wordList - set([beginWord])
        
        while len(que)!=0:
            delete = set()
            for word in wordList:
                flag = 0
                for i in range(len(beginWord)):
                    if(que[-1][0][i]!=word[i]):
                        flag += 1
                        if(flag==2):
                            break
                if(flag==1):
                    que.appendleft((word, que[-1][1] + 1))
                    delete.add(word)
            wordList = wordList - delete
            ans = que[-1][1]
            if(que.pop()[0]==endWord):
                check = True
                break
                
        if(check):
            return ans
        else:
            return 0