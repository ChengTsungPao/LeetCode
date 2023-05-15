class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        count = [0] * 26
        for ch in tiles:
            count[ord(ch) - ord("A")] += 1
            
        def recur(count):            
            ans = 0
            for i in range(26):
                if count[i] > 0:
                    count[i] -= 1
                    ans += 1 + recur(count)
                    count[i] += 1
            return ans
        
        return recur(count)