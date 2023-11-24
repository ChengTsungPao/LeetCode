class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        '''
        |x - y| <= min(x, y)
        
        if x >= y
            x - y <= y => x <= 2y
        '''
        
        ans = 0
        for i in range(20, -1, -1):
            ans <<= 1
            
            prefixMin = collections.defaultdict(lambda: float("inf"))
            prefixMax = collections.defaultdict(lambda: -float("inf"))
            for num in nums:
                shiftNum = num >> i
                prefixMin[shiftNum] = min(prefixMin[shiftNum], num)
                prefixMax[shiftNum] = max(prefixMax[shiftNum], num)
                
            for x in prefixMin:
                y = ans ^ 1 ^ x
                if y in prefixMin and x >= y and prefixMin[x] <= 2 * prefixMax[y]:
                    ans |= 1
                    break
                    
        return ans