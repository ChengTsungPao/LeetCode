class Solution:
    def reachNumber(self, target: int) -> int:        
        ''' 
        6  =  1 + 2 + 3 ------------------- 3
        
        7  =  1 + 2 + 3 - 4 + 5 ----------- 5
        
        8  = -1 + 2 + 3 + 4 --------------- 4
        
        9  =  1 + 2 - 3 + 4 + 5 ----------- 5
        
        10 =  1 + 2 + 3 + 4 --------------- 4
        
        11 =  1 - 2 + 3 + 4 + 5 ----------- 5
        
        12 =  1 + 2 - 3 + 4 + 5 - 6 - 7 --- 7
        
        13 = -1 + 2 + 3 + 4 + 5 ----------- 5
        
        14 =  1 + 2 + 3 + 4 + 5 + 6 - 7 --- 7
        
        15 =  1 + 2 + 3 + 4 + 5 ----------- 5
        '''
        
        def solve(target):
            # n(n + 1) ~ target * 2
            return math.ceil((-1 + (1 + 8 * target) ** 0.5) / 2)
        
        target = abs(target)
        
        n = solve(target)
        _sum = n * (n + 1) // 2
        
        if (_sum - target) % 2 == 0:
            return n
        
        if (n + 1) % 2 == 0:
            return n + 2
        else:
            return n + 1