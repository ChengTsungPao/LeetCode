class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        
        m = len(primes)
        
        heap = []
        for i, prime in enumerate(primes):
            heap.append((prime, prime, 1))
        
        heapq.heapify(heap)
        
        ans = [1]
        for _ in range(1, n):

            num, prime, index = heapq.heappop(heap)
            while heap and num == heap[0][0]:
                heapq.heappush(heap, (ans[index] * prime, prime, index + 1))
                num, prime, index = heapq.heappop(heap)
            
            ans.append(num)
            heapq.heappush(heap, (ans[index] * prime, prime, index + 1))

        return ans[n - 1]