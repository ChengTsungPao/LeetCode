class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
            
        slow1 = nums[0]
        slow2 = fast
        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
            
        return slow1