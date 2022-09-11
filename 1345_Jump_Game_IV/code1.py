class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        n = len(arr)
        
        numIndex = collections.defaultdict(list)
        for i, num in enumerate(arr):
            numIndex[num].append(i)
            
        
        que = collections.deque([(n - 1, 0)])
        visited = set([n - 1])
        
        while que:
            index, step = que.pop()
            
            if index == 0:
                return step
            
            num = arr[index]
            for nextIndex in numIndex[num] + [index + 1, index - 1]:
                if not (0 <= nextIndex < n) or nextIndex in visited:
                    continue
                    
                que.appendleft((nextIndex, step + 1))
                visited.add(nextIndex)
                
            numIndex[num] = []
                
        return -1