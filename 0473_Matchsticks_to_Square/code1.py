class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        totalSum = sum(matchsticks)
        if totalSum % 4 > 0:
            return False
        
        length = totalSum // 4
        status = [length] * 4
        
        matchsticks.sort(reverse = True)
        
        memo = set()
        def recur(index, status):
            key = str(index) + "_" + str(sorted(status))
            
            if key not in memo:
                if min(status) < 0:
                    return False
                elif sum(status) == 0:
                    return True
                
                for i in range(4):
                    status[i] -= matchsticks[index]
                    if recur(index + 1, status):
                        return True
                    status[i] += matchsticks[index]
                    
                memo.add(key)
                
            return False
        
        return recur(0, status)