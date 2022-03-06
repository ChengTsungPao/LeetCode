class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = collections.Counter(nums)
        
        bucket = collections.defaultdict(list)
        minFrequence = float("inf")
        maxFrequence = -float("inf")
        for num, frequence in count.items():
            bucket[frequence].append(num)
            minFrequence = min(minFrequence, frequence)
            maxFrequence = max(maxFrequence, frequence)
        
        ans = []
        for frequence in range(maxFrequence, minFrequence - 1, -1):
            k -= len(bucket[frequence])
            ans += bucket[frequence]
            if k <= 0:
                break
                
        return ans