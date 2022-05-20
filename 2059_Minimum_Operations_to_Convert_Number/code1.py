class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        
        stack = [start]
        level = 1
        visited = set([start])
        
        while stack:
            
            newStack = []
            while stack:
                start = stack.pop()
                
                for num in nums:
                    for nextNum in [start ^ num, start + num, start - num]:
                        if nextNum == goal:
                            return level
                        if not (0 <= nextNum <= 1000) or nextNum in visited:
                            continue
                            
                        visited.add(nextNum)
                        newStack.append(nextNum)
                        
            stack = newStack 
            level += 1
            
        return -1