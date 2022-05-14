class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        
        ans = 0
        bitmask = 0
        count = collections.defaultdict(int)
        count[0] = 1
        
        for ch in word:
            bitmask ^= 1 << (ord(ch) - 97)
            ans += count[bitmask]
            for i in range(10):
                ans += count[bitmask ^ (1 << i)]
            count[bitmask] += 1
            
        return ans