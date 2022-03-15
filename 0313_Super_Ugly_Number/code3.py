class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        uglyNums = [1]
        index_of_prime = [0] * len(primes)

        heap = []
        for i in range(len(primes)):
            candidateNum = uglyNums[index_of_prime[i]] * primes[i]
            heap.append((candidateNum, i))

        i = 0
        while i < n - 1:
            number, index = heapq.heappop(heap)

            if number > uglyNums[-1]:
                uglyNums.append(number)
                i += 1
                
            index_of_prime[index] += 1

            candidateNum = uglyNums[index_of_prime[index]] * primes[index]
            heapq.heappush(heap, (candidateNum, index))

        return uglyNums[-1]