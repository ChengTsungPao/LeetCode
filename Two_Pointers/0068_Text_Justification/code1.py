class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        n = len(words)
        
        def combineWords(i, j, sentence_len):
            if j - i - 1 == 0:
                return words[i] + " " * (maxWidth - len(words[i]))
            remainder = maxWidth - sentence_len
            q, r = remainder // (j - i - 1), remainder % (j - i - 1)
            sentence = words[i]
            for k in range(i + 1, j):
                sentence += " " * (1 + q + (r > 0)) + words[k]
                r -= 1
            return sentence
        
        ans = []
        i = 0
        while i < n:
            j = i + 1
            sentence_len = len(words[i])
            while j < n and sentence_len + len(words[j]) + 1 <= maxWidth:
                sentence_len += len(words[j]) + 1
                j += 1
                
            if j < n:
                ans.append(combineWords(i, j, sentence_len))
            else:
                ans.append(" ".join(words[i: j]) + " " * (maxWidth - sentence_len))    
            i = j
            
        return ans