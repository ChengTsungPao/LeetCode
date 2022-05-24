class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        n = len(rains)
        
        index = {}
        for i, rain in enumerate(rains):
            if rain not in index:
                index[rain] = collections.deque()
            else:
                index[rain].appendleft(i)
        
        ans = []
        heap = []
        cache = set()
        for i, rain in enumerate(rains):   
            if rain in cache:
                return []
            
            if rain > 0:
                ans.append(-1)
                if index[rain]:
                    heapq.heappush(heap, (index[rain].pop(), rain))
                    cache.add(rain)
            else:
                if heap:
                    i_, rain_ = heapq.heappop(heap)
                    cache.remove(rain_)
                    ans.append(rain_)
                else:
                    ans.append(1)
            
        return ans