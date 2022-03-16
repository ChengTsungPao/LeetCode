class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = collections.Counter(tasks)
        
        # Ready Heap
        heap = [(-v, k) for (k, v) in count.items()]
        heapq.heapify(heap)
        
        # IDLE Queue
        cooldown = collections.deque([(0, "")] * n)
        
        time = index = 0
        while index < len(tasks): 
            if heap:
                frequence, task = heapq.heappop(heap)
                frequence += 1
                cooldown.appendleft((frequence, task))
                
                index += 1
            else:
                cooldown.appendleft((0, ""))
                
            preFrequence, preTask = cooldown.pop()
            if preFrequence != 0:
                heapq.heappush(heap, (preFrequence, preTask))
                
            time += 1

        return time