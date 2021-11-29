class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        def compare(word1, word2):
            i = j = 0
            
            while i < len(word1) and j < len(word2):
                if word1[i] == word2[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
                    
            return j == len(word2)
        
        constraint_length = 1000
        dictionary.sort(key = lambda element: (constraint_length - len(element), element))
        
        for word in dictionary:
            if compare(s, word):
                return word
            
        return ""