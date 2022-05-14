class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        
        ans = 1
        remainder = 1
        cache = set()
        
        while remainder > 0:
            if remainder < k:
                remainder = 10 * remainder + 1
                ans += 1
                continue
                
            remainder %= k
            
            if remainder in cache:
                return -1
            cache.add(remainder)
            
        return ans