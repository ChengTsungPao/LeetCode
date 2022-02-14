class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        from sortedcontainers import SortedList
        
        if k == 0:
            return False
        
        tree = SortedList()
        tree.add(nums[0])
        
        i = 0
        j = 1
        while j < len(nums):                
            if tree.bisect_left(nums[j] - t) != tree.bisect_right(nums[j] + t):
                return True
            
            tree.add(nums[j])    
            j += 1
            
            if j - i > k:
                tree.remove(nums[i])
                i += 1
        
        return False