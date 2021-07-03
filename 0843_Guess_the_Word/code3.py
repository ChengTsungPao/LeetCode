# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        
        def compare(word1, word2, count):
            for i in range(len(word1)):
                if word1[i] == word2[i]:
                    count -= 1
            return count == 0
        
        status = collections.defaultdict(int)
        for word in wordlist:
            for i in range(len(word)):
                status[i, word[i]] += 1
                
        while wordlist:
            
            # 計算相關性
            max_score = -float("inf")
            for word in wordlist:
                score = 0
                for i in range(len(word)):
                    score += status[i, word[i]]
                
                if score > max_score:
                    max_score = score
                    chooseWord = word
            
            wordlist.remove(chooseWord)
            count = master.guess(chooseWord)
            if count == -1:
                count = 0
            
            newWordlist = []
            for i in range(len(wordlist)):
                if compare(chooseWord, wordlist[i], count):
                    newWordlist.append(wordlist[i])
                    
            wordlist = newWordlist.copy()   
