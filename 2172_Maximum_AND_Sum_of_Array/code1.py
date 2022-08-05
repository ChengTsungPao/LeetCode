class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        
        n = len(nums)
        c = 2 ** (2 * numSlots) - 1
        
        memo = {}
        def recur(index, slotBitmask):
            
            if (index, slotBitmask) not in memo:
            
                if slotBitmask >= c or index >= n:
                    return 0

                ret = recur(index + 1, slotBitmask)
                for slot in range(1, numSlots + 1):
                    if slotBitmask & (1 << (2 * slot - 1)) > 0:
                        continue
                    ret = max(ret, (slot & nums[index]) + recur(index + 1, slotBitmask + (1 << (2 * slot - 2))))
                    
                memo[index, slotBitmask] = ret
                
            return memo[index, slotBitmask]
        
        return recur(0, 0)