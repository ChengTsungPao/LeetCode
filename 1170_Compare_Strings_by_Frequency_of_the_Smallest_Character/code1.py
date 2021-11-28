class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:     
        
        for i in range(len(words)):
            words[i] = words[i].count(min(words[i]))  
            
        words.sort()
        
        ans = []
        for i in range(len(queries)):
            queries[i] = queries[i].count(min(queries[i]))
            ans.append(len(words) - bisect.bisect_right(words, queries[i]))

        return ans