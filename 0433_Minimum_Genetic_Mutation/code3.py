class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        if end not in bank:
            return -1
        
        
        def validChange(genetic1, genetic2, memo = {}):
            count = 0
            for i in range(8):
                if genetic1[i] != genetic2[i]:
                    count += 1
            return count == 1
        
        def update(genetic, step, cache, que):
            for nextGenetic in bank:
                if nextGenetic in cache or not validChange(genetic, nextGenetic):
                    continue
                    
                cache[nextGenetic] = step + 1
                que.appendleft((nextGenetic, step + 1))
        
        
        que1 = collections.deque([(start, 0)])
        que2 = collections.deque([(end, 0)])
        cache1 = {start: 0}
        cache2 = {end: 0}
        
        while que1 or que2:
            
            if que1:
                genetic1, step1 = que1.pop()
                
                if genetic1 in cache2:
                    return cache2[genetic1] + step1
                
                update(genetic1, step1, cache1, que1)
            
            if que2:
                genetic2, step2 = que2.pop()
                
                if genetic2 in cache1:
                    return cache1[genetic2] + step2
                
                update(genetic2, step2, cache2, que2)

        return -1 