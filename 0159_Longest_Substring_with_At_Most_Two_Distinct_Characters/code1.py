class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        
        orderedDict = collections.OrderedDict()
        ans = i = j = 0
        
        while j < len(s):
            
            if s[j] in orderedDict:
                orderedDict.move_to_end(s[j])
            orderedDict[s[j]] = j

            if len(orderedDict) > 2:
                i = orderedDict.popitem(last = False)[1] + 1         
            
            ans = max(ans, j - i + 1) 
            
            j += 1
            
        return ans   