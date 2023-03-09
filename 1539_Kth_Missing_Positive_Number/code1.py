class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        preNum = 0
        for num in arr:
            if num - preNum - 1 >= k:
                return preNum + k
            k -= (num - preNum - 1)
            preNum = num
        
        return arr[-1] + k