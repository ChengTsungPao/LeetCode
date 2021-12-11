class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        maxZeroLength = 0
        preIndex = -1
        
        for index in range(len(seats)):
            
            if seats[index] == 1:
                length = index - preIndex - 1
                maxZeroLength = max(maxZeroLength, length if preIndex >= 0 else length * 2)
                preIndex = index
                
        length = len(seats) - preIndex - 1        
        maxZeroLength = max(maxZeroLength, length * 2)

        return maxZeroLength // 2 if maxZeroLength % 2 == 0 else (maxZeroLength + 1) // 2