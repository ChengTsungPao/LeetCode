class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            if(stones[-1] != stones[-2]):
                stones.insert(bisect.bisect_left(stones, stones[-1] - stones[-2]), stones.pop() - stones.pop())
            else:
                stones.pop()
                stones.pop()
                
        if(stones == []):
            return 0
        else:
            return stones[0]