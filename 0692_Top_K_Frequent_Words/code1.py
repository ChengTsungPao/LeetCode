class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        ans, status = [], []
        
        count = collections.Counter(words)
        for key in count.keys():
            status.append((-count[key], key))
        
        heapq.heapify(status)
        for i in range(k):
            ans.append(heapq.heappop(status)[1])
    
        return ans