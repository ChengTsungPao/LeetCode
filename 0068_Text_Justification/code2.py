class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        n = len(words)
        
        def combine(i, j, sentence_length):
            if i == j:
                return words[i] + " " * (maxWidth - sentence_length)
            
            r = (maxWidth - sentence_length) % (j - i)
            d = (maxWidth - sentence_length) // (j - i)

            ret = words[i]
            for k in range(i + 1, j + 1):
                ret += " " * (d + (r > 0)) + words[k]
                r -= 1
                
            return ret

        
        ans = []
        i, cur_length = 0, -1
        for j in range(n):
            cur_length += 1 + len(words[j])
            
            if cur_length > maxWidth:
                ans.append(combine(i, j - 1, cur_length - len(words[j]) - (j - i)))
                cur_length = len(words[j])
                i = j
        
        ans.append(" ".join(words[i: n]))
        ans[-1] += " " * (maxWidth - len(ans[-1]))
        
        return ans