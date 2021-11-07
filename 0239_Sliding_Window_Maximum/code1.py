class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        inValid = {} # 紀錄在heap中的無效element
        
        nums = [-float("inf")] + nums
        heap = [-nums[i] for i in range(k)]
        heapq.heapify(heap)
        
        ans = []
        
        for i in range(k, len(nums)):
            
            inValidElement = nums[i - k]
            inValid[inValidElement] = inValid.get(inValidElement, 0) + 1
            
            heapq.heappush(heap, -nums[i])
            
            while inValid.get(-heap[0], 0) > 0:
                inValid[-heap[0]] -=  1
                heapq.heappop(heap)
            _max = -heap[0]
                
            ans.append(_max)
            
        return ans