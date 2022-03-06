class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:     
        
        # calculate f(s)
        for i in range(len(words)):
            words[i] = words[i].count(min(words[i]))  
            
        for i in range(len(queries)):
            queries[i] = queries[i].count(min(queries[i]))

        # bucket
        frequence = [0] * (max(words) + 1)
        for word in words:
            frequence[word] += 1
        
        # preSum
        for i in range(1, len(frequence)):
            frequence[i] += frequence[i - 1]
        
        # Answer
        ans = []
        for querie in queries:
            if querie < len(frequence):
                ans.append(frequence[-1] - frequence[querie])
            else:
                ans.append(0)
        
        return ans