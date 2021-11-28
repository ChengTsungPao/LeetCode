class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        stack = []
        
        for start, end in sorted(intervals):
            
            if stack and stack[-1][0] <= start <= stack[-1][1]:
                stack[-1][1] = max(end, stack[-1][1])
            else:
                stack.append([start, end])
                
        return stack