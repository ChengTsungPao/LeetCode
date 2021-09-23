class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        def arrival_time(index):
            return (target - data[index][0]) / data[index][1]
        
        data = sorted(zip(position, speed))
        ans, i, j = len(data), len(data) - 2, len(data) - 1

        while i >= 0:
            if arrival_time(i) <= arrival_time(j):
                ans -= 1
            else:
                j = i
            i -= 1
                
        return ans
