class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def validChange(genetic1, genetic2, memo = {}):
            count = 0
            for i in range(8):
                if genetic1[i] != genetic2[i]:
                    count += 1
            return count == 1
        
        
        que = collections.deque([(start, 0)])
        visited = set([start])
        
        while que:
            genetic, step = que.pop()
            
            if genetic == end:
                return step
            
            for nextGenetic in bank:
                if nextGenetic in visited or not validChange(genetic, nextGenetic):
                    continue
                    
                visited.add(nextGenetic)
                que.appendleft((nextGenetic, step + 1))
        
        return -1 