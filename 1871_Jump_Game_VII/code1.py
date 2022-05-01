class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        n = len(s)
        
        curMax = 0
        que = collections.deque([0])
        
        while que:
            index = que.pop()
            
            for nextIndex in range(max(curMax, index + minJump), min(index + maxJump + 1, n)):
                if s[nextIndex] == "1":
                    continue
                    
                if nextIndex == n - 1:
                    return True
                    
                que.appendleft(nextIndex)
                
            curMax = max(curMax, index + maxJump + 1)
            
        return False