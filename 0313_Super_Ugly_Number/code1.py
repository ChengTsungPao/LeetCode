class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        heap = []
        for index in range(len(primes)):
            heap.append((primes[index], index))

        number = 1
        for _ in range(n - 1):
            number, index = heapq.heappop(heap)

            for i in range(index, len(primes)):
                heapq.heappush(heap, (number * primes[i], i))

        return number