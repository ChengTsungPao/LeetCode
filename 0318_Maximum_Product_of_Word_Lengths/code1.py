class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        def compare(word1, word2):
            word2 = set(word2)
            for ch in word1:
                if ch in word2:
                    return False
            return True
        
        words.sort(key = len, reverse = True)
        
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if compare(words[i], words[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
                    break
                    
        return ans