class Heap: 
    
    def __init__(self, heap):
        self.heap = heap
        
    def heappush(self, num):
        self.heap.append(num)
        self.heapifyAll()
        
    def heappop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        ret = self.heap.pop()
        self.heapifyAll()
        return ret
        
    def heapifyAll(self): # Bottom up
        for index in range(len(self.heap) // 2, -1, -1): 
            self.heapify(index)
    
    def heapify(self, index):
        minIndex = index
        left, right = index * 2, index * 2 + 1
        
        if left < len(self.heap) and self.heap[minIndex] > self.heap[left]:
            minIndex = left
            
        if right < len(self.heap) and self.heap[minIndex] > self.heap[right]:
            minIndex = right
        
        if minIndex != index:
            self.heap[index], self.heap[minIndex] = self.heap[minIndex], self.heap[index]
            self.heapify(minIndex)
            
            
class Solution:
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 方法: 限定min heap的長度為k，其中heap的頭為當前第k大的數字
        # 備註: 先heapify前k個num可加速 (heapifyAll => time: O(n), heappush => time: O(logn))
        
        heapq = Heap(copy.copy(nums[:k]))
        heapq.heapifyAll()
        
        for i in range(k, len(nums)):
            heapq.heappush(nums[i])
            heapq.heappop()

        return heapq.heap[0]
