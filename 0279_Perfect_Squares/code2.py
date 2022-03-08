class Solution:
    def numSquares(self, n: int) -> int:
        dp = set([n])
        que = collections.deque()
        que.appendleft((n, 1, float("inf")))
        
        while que:
            num, step, index = que.pop()
            
            for i in range(min(int(num ** 0.5), index), 0, -1):
                if num - i ** 2 == 0:
                    return step
                
                if num - i ** 2 not in dp:
                    que.appendleft((num - i ** 2, step + 1, i))
                    dp.add(num - i ** 2)
                    
        return -1