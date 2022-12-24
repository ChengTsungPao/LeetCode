class Solution:
    def smallestValue(self, n: int) -> int:

        len_of_prime = n + 1
        prime = [True] * len_of_prime    
        prime[0] = prime[1] = False
        for i in range(2, len_of_prime):
            if prime[i]:
                j = i * i
                while j < len_of_prime:
                    prime[j] = False
                    j += i
        
        def operation(n):
            s = 0
            for i in range(2, len_of_prime):
                if i > n: break
                while i <= n and prime[i] and n % i == 0:
                    n //= i
                    s += i
            return s
        
        cache = set([n])
        while not prime[n]:
            n = operation(n)
            if n in cache:
                break
            cache.add(n)
            
        return n