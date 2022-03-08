class Solution:
    def numSquares(self, n: int) -> int:
        que = set([n])
        step = 0
        
        while que:
            newQue = set()
            
            while que:
                num = que.pop()
                
                if num == 0:
                    return step

                for i in range(int(num ** 0.5), 0, -1):
                    newQue.add(num - i ** 2)
                    
            step += 1        
            que = newQue
                    
        return -1