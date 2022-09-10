class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        
        total = sum(nums)
        if total % k != 0:
            return False
        
        status = [total // k] * k
        
        memo = set()
        def recur(index):
            
            key = str(sorted(status)) + "_" + str(index)
            
            if key not in memo:
            
                if min(status) < 0:
                    return False
                elif sum(status) == 0:
                    return True

                for i in range(k):
                    status[i] -= nums[index]
                    if recur(index + 1):
                        return True
                    status[i] += nums[index]
                    
                memo.add(key)
                
            return False
        
        nums.sort(reverse = True)
        return recur(0)