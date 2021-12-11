class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        left = []
        preOneIndex = -float("inf")
        for i in range(len(seats)):
            if seats[i] == 1:
                preOneIndex = i
            left.append(i - preOneIndex)
            
        right = []
        nextOneIndex = float("inf")
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 1:
                nextOneIndex = i
            right.append(nextOneIndex - i)  
        right = right[::-1]
            
        ans = 0
        for i in range(len(left)):
            ans = max(ans, min(left[i], right[i]))

        return ans