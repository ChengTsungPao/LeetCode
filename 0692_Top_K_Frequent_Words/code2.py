class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        count = collections.Counter(words)
        
        bucket = collections.defaultdict(list)
        minFrequence = float("inf")
        maxFrequence = -float("inf")
        for num, frequence in count.items():
            bucket[frequence].append(num)
            minFrequence = min(minFrequence, frequence)
            maxFrequence = max(maxFrequence, frequence)
        
        ans = []
        for frequence in range(maxFrequence, minFrequence - 1, -1):
            for word in sorted(bucket[frequence])[:k]:
                ans.append(word)
            k -= len(bucket[frequence])
            if k <= 0:
                break
                
        return ans