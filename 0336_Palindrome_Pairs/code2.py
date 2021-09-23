class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        # 找prefix和suffix是否在wordDict裡面，在check剩下的word是否為Palindrome
        # 由於Constraints，所以造成O(N*k**2)會比O(k*N**2)快速
        
        # Constraints:
        # 1 <= words.length <= 5000   => N
        # 0 <= words[i].length <= 300 => k
        
        wordDict = {}
        for i in range(len(words)):
            wordDict[words[i]] = i
        
        ans = []
        if "" in wordDict:
            for i in range(len(words)):
                if wordDict[""] != i and self.isPalindrome(words[i], 0, len(words[i]) - 1):
                    ans.append([i, wordDict[""]])
                    ans.append([wordDict[""], i])
        
        for i in range(len(words)):
            word = words[i]
            wordLength = len(word)
            startStr = endStr = ""
            
            for j in range(len(word)):
                start, end = j, wordLength - j - 1
                startStr, endStr = word[start] + startStr, endStr + word[end]
                if startStr in wordDict and wordDict[startStr] != i and self.isPalindrome(word, start + 1, wordLength - 1):
                    ans.append([i, wordDict[startStr]])
                if j != wordLength - 1 and endStr in wordDict and wordDict[endStr] != i and self.isPalindrome(word, 0, end - 1):
                    ans.append([wordDict[endStr], i])  
                    
        return ans
                
    def isPalindrome(self, word, left, right):
        while left < right:
            if word[left] != word[right]:
                return False
            else:
                left += 1
                right -= 1
        return True