class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        ans = i = 0
        index = {}
        
        for j, num in enumerate(nums):
            
            d = 0
            while num > 0:
                if num & 1:
                    if d in index:
                        i = max(i, index[d] + 1)
                    index[d] = j
                    
                num >>= 1
                d += 1
            
            ans = max(ans, j - i + 1)
            
        return ans