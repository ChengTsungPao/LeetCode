class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def combinationSum2(candidates, target):
            candidates = collections.Counter(candidates)
            number = list(candidates.keys())
            
            def recur(target, index, memo = {}):
                if target == 0:
                    return True
                elif target < 0 or index == len(number):
                    return False
                
                if (target, index, candidates[number[index]]) not in memo:
                    memo[target, index, candidates[number[index]]] = False
                    for i in range(index, len(number)):
                        if candidates[number[i]] != 0:
                            candidates[number[i]] -= 1
                            if recur(target - number[i], i, memo):
                                memo[target, index, candidates[number[index]]] =  True
                                break
                            candidates[number[i]] += 1
                            
                return memo[target, index, candidates[number[index]]]
            
            return recur(target, 0) 
        
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        else:
            return combinationSum2(nums, total // 2)