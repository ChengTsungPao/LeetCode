class Solution:
    def trap(self, height: List[int]) -> int:
        
        ans, stack = 0, [(0, 0)]
        
        for i in range(len(height)):
            
            count, minHeight = 1, min(stack[0][0], height[i])
            while stack and stack[-1][0] < height[i]:
                element = stack.pop()
                ans += (minHeight - element[0]) * element[1]
                count += element[1]
                
            stack.append((height[i], count))

        return ans