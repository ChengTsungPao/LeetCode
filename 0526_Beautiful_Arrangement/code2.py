class Solution:
    def countArrangement(self, n: int) -> int:
        
        valid = collections.defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    valid[i].append(j)
        
        memo = {}
        def recur(i, bitmask = 0):
            
            if (i, bitmask) not in memo:
            
                if i >= n + 1:
                    return 1

                ans = 0
                for j in valid[i]:
                    if (bitmask >> j) & 1:
                        continue

                    bitmask += (1 << j)
                    ans += recur(i + 1, bitmask)
                    bitmask -= (1 << j)
                    
                memo[i, bitmask] = ans
                
            return memo[i, bitmask]
        
        return recur(1)