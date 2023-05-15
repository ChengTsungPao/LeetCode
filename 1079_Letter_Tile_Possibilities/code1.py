class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        count = [0] * 26
        for ch in tiles:
            count[ord(ch) - ord("A")] += 1
            
        def getStrNums(status):
            _sum = sum(status)
            if _sum == 0: 
                return 0
            ans = math.factorial(_sum)
            for c in status:
                ans //= math.factorial(c)
            return ans
            
        def recur(idx, status):
            if idx >= 26:
                return 0
            
            ans = recur(idx + 1, status)
            for c in range(1, count[idx] + 1):
                status[idx] += c
                ans += getStrNums(status) + recur(idx + 1, status)
                status[idx] -= c
                
            return ans
        
        return recur(0, [0] * 26)