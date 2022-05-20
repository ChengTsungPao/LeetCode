class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        sorted_arr = sorted(zip(quality, wage), key = lambda x: (x[1] / x[0], x[1]))
        n = len(sorted_arr)
        
        qSum = 0
        heap = []
        for i in range(k - 1):
            q, w = sorted_arr[i]
            heap.append(-q)
            qSum += q
            
        heapq.heapify(heap)
            
        ans = float("inf")    
        for i in range(k - 1, n):
            q, w = sorted_arr[i]
            ans = min(ans, (w / q) * (qSum + q))
            
            qSum += q
            heapq.heappush(heap, -q)
            qSum += heapq.heappop(heap)

        return ans