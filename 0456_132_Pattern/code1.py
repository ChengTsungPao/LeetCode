class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        from sortedcontainers import SortedList
        
        n = len(nums)
        bst = SortedList(nums)
        
        numi = nums[0]
        bst.remove(numi)
        
        for j in range(1, n):
            
            numj = nums[j]
            bst.remove(numj)
            
            k = bst.bisect_left(numj) - 1
            if k >= 0 and numi < bst[k] < numj:
                return True

            numi = min(numi, numj)
            
        return False