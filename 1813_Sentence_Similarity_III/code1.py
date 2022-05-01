class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        
        sentence1 = sentence1.split(" ")
        sentence2 = sentence2.split(" ")
        
        m = len(sentence1)
        n = len(sentence2)
        
        # len(sentence1) >= len(sentence2)
        def check(sentence1, sentence2):
            i = 0
            j = len(sentence2) - 1
            for k in range(len(sentence1)):
                if k < len(sentence2) and sentence1[k] == sentence2[i]:
                    i += 1
                else:
                    break  
            _min = k
            for k in range(len(sentence1) - 1, _min, -1):
                if k >= 0 and sentence1[k] == sentence2[j]:
                    j -= 1
                else:
                    break 
            return i > j
        
        if m >= n:
            return check(sentence1, sentence2)
        else:
            return check(sentence2, sentence1)