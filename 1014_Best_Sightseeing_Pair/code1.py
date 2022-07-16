class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        n = len(values)
        
        ans = max_ = -float("inf")
        for j in range(n):
            ans = max(ans, max_ + values[j] - j)
            max_ = max(max_, values[j] + j)
        
        return ans