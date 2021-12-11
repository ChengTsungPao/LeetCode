class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        # 概念: 想成有幾個連續區塊要塗顏色 (n = 1 + 2 + 1 + 2 + 1...)
        
        def calculate(countOne, countTwo):
            total = countOne + countTwo
            return math.comb(total, countTwo) * k * (k - 1) ** (total - 1)
        
        
        ans = 0
        countOne, countTwo = n, 0
        
        while countOne >= 0:
            ans += calculate(countOne, countTwo)
            countOne, countTwo = countOne - 2, countTwo + 1
            
        return ans
