class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key = lambda element: element[1])
        
        def find_max(width, count, index, envelope):
            
            ans = 0
            
            for i in range(index, len(width)):
                
                if width[i] != envelope:
                    
                    ans = max(ans, count[i])
                    
            return ans
        
        
        def lengthOfLIS(envelopes):

            ans, height, width, count = 1, [envelopes[-1][0]], [envelopes[-1][1]], [1]
            
            for i in range(len(envelopes) - 2, -1, -1):

                index = bisect.bisect_right(height, envelopes[i][0])

                count.insert(index, find_max(width, count, index, envelopes[i][1]) + 1)
                width.insert(index, envelopes[i][1])
                height.insert(index, envelopes[i][0])

                ans = max(ans, count[index])

            return ans
        
        return lengthOfLIS(envelopes)
        