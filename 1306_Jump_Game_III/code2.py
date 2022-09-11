class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)

        stack = [start]
        visited = set([start])
        
        while stack:
            index = stack.pop()
            
            num = arr[index]
            if num == 0:
                return True
            
            for nextIndex in [index - num, index + num]:
                if not (0 <= nextIndex < n) or nextIndex in visited:
                    continue
                    
                stack.append(nextIndex)
                visited.add(nextIndex)
                
        return False