class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        
        for _ in range(k):
            pile = heapq.heappop(piles)
            heapq.heappush(piles, math.floor(pile / 2))
            
            if pile == 0:
                break
            
        return -sum(piles)