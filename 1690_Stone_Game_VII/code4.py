class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = [0] + nums
        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i - 1]
        
    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j + 1] - self.nums[i]

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        obj = NumArray(stones)
        
        dp = collections.defaultdict(int)
        
        for w in range(1, len(stones)):
            
            for s in range(0, len(stones) - w):
                
                i, j = s, s + w  
                
                dp[i, j] = max(obj.sumRange(i + 1, j) - dp[i + 1, j], obj.sumRange(i, j - 1) - dp[i, j - 1])
           
        return dp[0, len(stones) - 1]   