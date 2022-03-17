class Solution:
    def numSplits(self, s: str) -> int:
        
        ans = 0
        left = collections.Counter()
        right = collections.Counter(s)
        
        for ch in s:
            left[ch]  += 1
            right[ch] -= 1
            
            if right[ch] == 0:
                del right[ch]
            
            if len(left) == len(right):
                ans += 1
                
        return ans