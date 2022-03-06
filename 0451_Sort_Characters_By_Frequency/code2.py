class Solution:
    def frequencySort(self, s: str) -> str:
        
        count = collections.Counter(s)
        
        bucket = collections.defaultdict(list)
        minFrequence = float("inf")
        maxFrequence = -float("inf")
        for ch, frequence in count.items():
            bucket[frequence].append(ch)
            minFrequence = min(minFrequence, frequence)
            maxFrequence = max(maxFrequence, frequence)
        
        ans = ""
        for frequence in range(maxFrequence, minFrequence - 1, -1):
            for ch in sorted(bucket[frequence]):
                ans += ch * frequence
                
        return ans