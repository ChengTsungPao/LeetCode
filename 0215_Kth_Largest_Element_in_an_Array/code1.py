class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 方法: 限定min heap的長度為k，其中heap的頭為當前第k大的數字
        # 備註: 先heapify前k個num可加速 (heapify => time: O(n), heappush => time: O(logn))
        
        heap = copy.copy(nums[:k])
        heapq.heapify(heap)
        
        for i in range(k, len(nums)):
            heapq.heappush(heap, nums[i])
            heapq.heappop(heap)
            
        return heap[0]
