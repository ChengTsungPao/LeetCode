class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        def arrival_time(index):
            return (target - data[index][0]) / data[index][1]
        
        data, index = sorted(zip(position, speed)), len(position) - 2
        
        while index >= 0:
            if arrival_time(index + 1) >= arrival_time(index):
                data.pop(index)
            index -= 1
                
        return len(data)
        