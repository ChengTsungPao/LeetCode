class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        # sort robot & factory by position (greedy)
        robot = sorted(robot)
        factory = sorted([pos for pos, limit in factory for _ in range(limit)])
        
        r_len = len(robot)
        f_len = len(factory)
        
        # get next factory index (hash table)
        next_f = f_len
        next_f_dict = {}
        for i in range(f_len - 1, -1, -1):
            if i + 1 >= f_len or factory[i] != factory[i + 1]: 
                next_f = i + 1
            next_f_dict[i] = next_f
        
        # knapsack (recursion)
        @functools.lru_cache(None)
        def recur(r, f):
            
            if r == r_len:
                return 0
            elif f == f_len:
                return float("inf")
                    
            return min(recur(r, next_f_dict[f]), recur(r + 1, f + 1) + abs(robot[r] - factory[f]))
        
        return recur(0, 0)