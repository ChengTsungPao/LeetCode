class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        
        heap = [(-nums[i], i) for i in range(k - 1)]
        heapq.heapify(heap)
        
        ans = []
        for i in range(k - 1, n):
            heapq.heappush(heap, (-nums[i], i))
            while heap and heap[0][1] <= i - k:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
            
        return ans