class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def recur(target):
            
            if target not in memo:
            
                if target < 0:
                    return 0
                elif target == 0:
                    return 1

                ret = 0
                for num in nums:
                    ret += recur(target - num)
                    
                memo[target] = ret
                
            return memo[target]
        
        return recur(target)