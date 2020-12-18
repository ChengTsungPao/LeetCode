class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def dfs(i, j, words, find, dp = {}):
            if (i, j) + find in dp or i < 0:
                return []
            words_empty, dp[(i, j) + find] = True, []
            for word in words.keys():
                if words[word] != 0:
                    if word == s[i - len(word) : i]:
                        words[word] -= 1
                        dp[(i, j) + find] += dfs(i - len(word), j, words, (len(word),) + find, dp)
                        words[word] += 1
                    if word == s[j : j + len(word)]:
                        words[word] -= 1
                        dp[(i, j) + find] += dfs(i, j + len(word), words, find + (len(word),), dp)
                        words[word] += 1
                    words_empty = False
            if words_empty:
                dp[(i, j) + find] = [i]
                return dp[(i, j) + find]
            else:
                return dp[(i, j) + find]
        
        ans = []
        index = 0
        word = words[0]
        words = collections.Counter(words)
        
        if len(words) == 1:
            temp = word
            word = word * words[word]
            words[temp] = 0
        else:
            words[word] -= 1
        
        while index < len(s):
            index = s.find(word, index, len(s))
            if index >= 0:
                ans += dfs(index, index + len(word), words, (len(word),))
                index += 1
            else:
                break
        
        return ans