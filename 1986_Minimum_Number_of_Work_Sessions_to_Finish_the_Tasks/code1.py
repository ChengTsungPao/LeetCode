class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        n = len(tasks)
        
        def getAllSubset(index):
            if index >= n:
                return [(0, 0)]
            
            ans = []
            for bitmask, _sum in getAllSubset(index + 1):
                if _sum <= sessionTime:
                    ans.append((bitmask, _sum))
                if _sum + tasks[index] <= sessionTime:
                    ans.append((bitmask | (1 << index), _sum + tasks[index]))
                    
            return ans
        
        subset = getAllSubset(0)
        
        memo = {}
        def recur(bitmask):
            
            if bitmask not in memo:
            
                if bitmask == 2 ** n - 1:
                    return 0

                ans = float("inf")
                for opr, _sum in subset:
                    if opr & bitmask > 0 or _sum == 0:
                        continue
                    ans = min(ans, 1 + recur(bitmask | opr))

                memo[bitmask] = ans
            
            return memo[bitmask]
        
        return recur(0)