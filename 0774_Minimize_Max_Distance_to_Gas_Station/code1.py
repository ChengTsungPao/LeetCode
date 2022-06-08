class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        
        n = len(stations)
        
        heap = []
        for i in range(n - 1):
            heap.append((-(stations[i + 1] - stations[i]), 1))
            
        heapq.heapify(heap)
        
        while k > 0:
            distance, cut = heapq.heappop(heap)
            distance = distance * cut / (cut + 1)
            heapq.heappush(heap, (distance, cut + 1))
            k -= 1
            
        return -heap[0][0]