class Solution:
    def maxProduct(self, words: List[str]) -> int:    
        charTable = {chr(ascii): 2 ** (ascii - 97) for ascii in range(97, 97 + 26)}
        
        bitmaps = []
        for _str in words:
            s = 0
            for ch in _str:
                s |= charTable[ch]
            bitmaps.append(s)
        
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1,len(words)):
                if bitmaps[i] & bitmaps[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        
        return ans