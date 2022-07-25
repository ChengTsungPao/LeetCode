class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def isValid(count):
            for c1, c2 in zip(count, count_t):
                if c1 < c2:
                    return False
            return True
        
        def asciiToIndex(ch):
            if ord(ch) >= ord("a"):
                return ord(ch) - ord("a")
            else:
                return ord(ch) - ord("A") + 26
            
        n = len(s)
        
        count_t = [0] * 52
        for ch in t:
            count_t[asciiToIndex(ch)] += 1
            
        i = 0
        index = (n, 2 * n + 1)
        count = [0] * 52
        for j in range(n):
            count[asciiToIndex(s[j])] += 1      
            while isValid(count):
                index = min(index, (i, j + 1), key = lambda x: x[1] - x[0])
                count[asciiToIndex(s[i])] -= 1
                i += 1
                
        return s[index[0]: index[1]]