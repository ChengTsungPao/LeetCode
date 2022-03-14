class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        uglyNums = [1]
        index_of_prime = [0] * len(primes)

        heap = []
        visited = set()
        for i in range(len(primes)):
            candidateNum = uglyNums[index_of_prime[i]] * primes[i]
            heap.append((candidateNum, i))
            visited.add(candidateNum)

        for _ in range(n - 1):
            number, index = heapq.heappop(heap)
            visited.remove(number)

            uglyNums.append(number)
            index_of_prime[index] += 1

            candidateNum = uglyNums[index_of_prime[index]] * primes[index]
            while candidateNum in visited:
                index_of_prime[index] += 1
                candidateNum = uglyNums[index_of_prime[index]] * primes[index]

            heapq.heappush(heap, (candidateNum, index))
            visited.add(candidateNum)

        return uglyNums[n - 1]
