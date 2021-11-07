class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans, stack = [0 for _ in range(len(temperatures))], []
        
        for temperature, index in zip(temperatures, range(len(temperatures))):
            
            while stack and stack[-1][0] < temperature:
                preTemperature, preIndex = stack.pop()
                ans[preIndex] = index - preIndex
                
            stack.append((temperature, index))
        
        return ans
 