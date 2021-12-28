class Solution:
    def longestStrChain(self, words: List[str]) -> int:
    
        def isChain(word1, word2):
            if len(word1) + 1 != len(word2):
                return False
            
            i = j = 0
            while j < len(word2):
                if i < len(word1) and word1[i] == word2[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
                    
            return j - i == 1
        
        
        ans = 1
        dp = [1]
        words.sort(key = len)
        
        for i in range(1, len(words)):
            dp.append(1)
            
            for j in range(i):
                if isChain(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
                    
            ans = max(ans, dp[i])

        return ans