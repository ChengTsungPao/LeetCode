class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # {bitmask: n}
        # comb(n, 2) => n(n - 1) // 2
        
        count = collections.Counter()
        for word in words:
            bitmask = 0
            for ch in set(word):
                bitmask += pow(2, ord(ch) - ord("a"))
            count[bitmask] += 1
            
        return sum([n * (n - 1) // 2 for n in count.values()])