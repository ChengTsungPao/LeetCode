class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        isRemove = True
        
        while isRemove:
            
            isRemove = False
            
            j = len(s) - 1
            for i in range(len(s) - 1, -1, -1):
                if s[i] == s[j] and j - i + 1 < k:
                    continue

                if s[i] == s[j] and j - i + 1 == k:
                    isRemove = True
                    s = s[:i] + s[j + 1:]
                    j = i - 1
                else:
                    j = i
        
        return s