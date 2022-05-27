class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        ans = 0
        for pos in left:
            ans = max(ans, pos)
            
        for pos in right:
            ans = max(ans, n - pos)
            
        return ans