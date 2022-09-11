class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)

        que = collections.deque([start])
        visited = set([start])
        
        while que:
            index = que.pop()
            
            num = arr[index]
            if num == 0:
                return True
            
            for nextIndex in [index - num, index + num]:
                if not (0 <= nextIndex < n) or nextIndex in visited:
                    continue
                    
                que.appendleft(nextIndex)
                visited.add(nextIndex)
                
        return False