class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        n = len(costs)
        
        if candidates * 2 >= n:
            return sum(sorted(costs)[:k])
        
        leftHeap = costs[:candidates].copy()
        rightHeap = costs[-candidates:].copy()
        
        heapq.heapify(leftHeap)
        heapq.heapify(rightHeap)
        
        i = candidates
        j = n - candidates - 1
        
        ans = 0
        while leftHeap and rightHeap and k > 0:            
            if leftHeap[0] <= rightHeap[0]:
                ans += heapq.heappop(leftHeap)
                if i <= j: 
                    heapq.heappush(leftHeap, costs[i])
                    i += 1
            else:
                ans += heapq.heappop(rightHeap)
                if i <= j: 
                    heapq.heappush(rightHeap, costs[j])
                    j -= 1
            k -= 1
                    
        while leftHeap and k > 0:            
            ans += heapq.heappop(leftHeap)
            if i <= j: 
                heapq.heappush(leftHeap, costs[i])
                i += 1
            k -= 1
                
        while rightHeap and k > 0:            
            ans += heapq.heappop(rightHeap)
            if i <= j: 
                heapq.heappush(rightHeap, costs[j])
                j -= 1
            k -= 1
            
        return ans 