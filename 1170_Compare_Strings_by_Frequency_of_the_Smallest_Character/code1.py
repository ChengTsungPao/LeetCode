class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:     
        ans = collections.deque()
        for i in range(len(words)):
            words[i] = words[i].count(min(words[i]))  
        words.sort()
        for i in range(len(queries)):
            queries[i] = queries[i].count(min(queries[i]))
            ans.append(len(words)-bisect.bisect_right(words,queries[i],0,len(words)))

        return ans