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


        while wordlist:
            
            chooseWord = wordlist.pop(random.randint(0, len(wordlist) - 1))
            count = master.guess(chooseWord)
                    
            newWordlist = []
            for i in range(len(wordlist)):
                if compare(chooseWord, wordlist[i], count):
                    newWordlist.append(wordlist[i])
                    
            wordlist = newWordlist.copy()  
