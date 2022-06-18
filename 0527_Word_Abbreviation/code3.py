class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        
        def getLongestCommonPrefix(word1, word2):
            index = 0
            while index < len(word1) and index < len(word2) and word1[index] == word2[index]:
                index += 1
            return index
        
        groups = collections.defaultdict(list)
        for index, word in enumerate(words):
            groups[len(word), word[0], word[-1]].append((word, index))
        
        ans = [""] * len(words)
        for (length, first, last), wordIndexList in groups.items():
            wordIndexList.sort()
            n = len(wordIndexList)
            
            LCP = [0] * n
            for i in range(1, n):
                word1, word2 = wordIndexList[i - 1][0], wordIndexList[i][0]
                LCP[i] = getLongestCommonPrefix(word1, word2)
                LCP[i - 1] = max(LCP[i - 1], LCP[i])
                
            for (word, index), p in zip(wordIndexList, LCP):
                size = length - 1 - (p + 1)
                if size > 1:
                    ans[index] = word[:p+1] + str(size) + last
                else:
                    ans[index] = word
            
        return ans