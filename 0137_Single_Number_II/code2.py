class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # 統計該bit有幾個數字為1
        
        symbol = 1 if sum(num < 0 for num in nums) % 3 == 0 else -1
        
        ans = 0
        for i in range(32):
            s = 0
            for num in nums:
                if ((abs(num) >> i) & 1) == 1:
                    s += 1
                    s %= 3
            if s != 0:
                ans += (1 << i)
                
        return symbol * ans