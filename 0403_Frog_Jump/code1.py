class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        goal = stones[-1]
        stones = set(stones)
        n = len(stones)
        
        memo = set()
        def recur(position, step):
            if (position, step) not in memo:
                
                if step <= 0:
                    return False
            
                if position not in stones:
                    return False
                
                if position == goal:
                    return True
                
                if recur(position + step - 1, step - 1) or \
                   recur(position + step + 0, step + 0) or \
                   recur(position + step + 1, step + 1):
                    return True

                memo.add((position, step))
            
            return False
        
        if 1 not in stones:
            return False
        
        return recur(1, 1)