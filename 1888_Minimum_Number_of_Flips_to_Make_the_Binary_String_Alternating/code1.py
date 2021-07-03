class Solution:
    def minFlips(self, s: str) -> int:
        
        odd, even = collections.defaultdict(int), collections.defaultdict(int)
        
        length = len(s)
        
        for i in range(len(s)):
            if i % 2 == 0:
                odd[s[i]] += 1
            else:
                even[s[i]] += 1
        
        s *= 2
        
        ans = min(odd["0"] + even["1"], odd["1"] + even["0"])
        
        for i in range(length):
            
            if length % 2 == 0:
                odd[s[i]] -= 1
                odd[s[i + length]] += 1                
            else:
                odd[s[i]] -= 1    
                even[s[i + length]] += 1
                
            odd, even = even, odd
            
            ans = min(ans, odd["0"] + even["1"], odd["1"] + even["0"])
            
        return ans
