'''
min max heap
Time: addNum: O(logn), findMedian: O(1)
Space: O(n)

method:
addNum => add min heap or max heap, update self.median
condition
    min size = n, max size = n + 1 
    (val --> maxHeap) => (maxHeap --> minHeap) and (val --> maxHeap) 
'''   

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.median = -float("inf")
        
        
    def addNum(self, num: int) -> None:
        
        minHeapSize = len(self.minHeap)
        maxHeapSize = len(self.maxHeap)
        
        if num > self.median:
            if minHeapSize > maxHeapSize:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            heapq.heappush(self.minHeap, num)
        else:
            if maxHeapSize > minHeapSize:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            heapq.heappush(self.maxHeap, -num)

        minHeapSize = len(self.minHeap)
        maxHeapSize = len(self.maxHeap)
        
        if (minHeapSize + maxHeapSize) % 2:
            if minHeapSize > maxHeapSize:
                self.median = self.minHeap[0]
            else:
                self.median = -self.maxHeap[0]
        else:
            self.median = (self.minHeap[0] - self.maxHeap[0]) / 2
            
        
    def findMedian(self) -> float:
        return self.median        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()