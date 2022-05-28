class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        
        heap = [(-value, label) for value, label in zip(values, labels)]
        heapq.heapify(heap)
        
        ans = 0
        count = collections.defaultdict(int)
        while heap and numWanted > 0:
            value, label = heapq.heappop(heap)
            if count[label] >= useLimit:
                continue
            
            ans -= value
            count[label] += 1
            numWanted -= 1
            
        return ans