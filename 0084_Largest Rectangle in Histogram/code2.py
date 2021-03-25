class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        ans = -float("inf")
        stack = []
        
        for i in range(len(heights)):
            
            count = 0
            while stack and stack[-1][0] > heights[i]:
                element = stack.pop()
                count += element[1]
                ans = max(ans, element[0] * count)
                
            stack.append((heights[i], count + 1))
            
        count = 0
        while stack:
            element = stack.pop()
            count += element[1]
            ans = max(ans, element[0] * count)
            
        return ans