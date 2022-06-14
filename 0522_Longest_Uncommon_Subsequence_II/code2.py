class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        n = len(strs)
        strs.sort(key = len, reverse = True)
        
        def isSubsequence(str1, str2):
            i = j = 0
            while i < len(str1) and j < len(str2):
                if str1[i] == str2[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            return i == len(str1)
        
        
        for i in range(n):
            
            isFindOtherSubsequence = False
            for j in range(n):
                if i == j:
                    continue
                    
                if isSubsequence(strs[i], strs[j]):
                    isFindOtherSubsequence = True
                    break
                    
            if not isFindOtherSubsequence:
                return len(strs[i])
            
        return -1