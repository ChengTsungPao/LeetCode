class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def countChar(word):
            count = []
            for s in word:
                if count == [] or count[-1][0] != s:
                    count.append([s, 1])
                else:
                    count[-1][1] += 1
            return count
        
        ans = 0
        
        countS = countChar(s)
        for word in words:
            countWord = countChar(word)
            
            if len(countS) != len(countWord):
                continue
            
            same = True
            for i in range(len(countS)):
                s_char, s_count = countS[i]
                word_char, word_count = countWord[i]
                if s_char != word_char or s_count < word_count:
                    same = False
                    break
                if s_count == 2 and word_count == 1:
                    same = False
                    break
                    
            ans += same
                
        return ans