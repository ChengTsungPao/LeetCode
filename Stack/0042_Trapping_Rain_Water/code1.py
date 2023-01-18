class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        ans, stack = 0, [(height[0], 1)]
        
        for i in range(1, n):
            
            minH, accumulate = min(height[i], stack[0][0]), 1
            while stack and stack[-1][0] < height[i]:
                h, a = stack.pop()
                ans += (minH - h) * a
                accumulate += a
                
            stack.append((height[i], accumulate))
            
        return ans