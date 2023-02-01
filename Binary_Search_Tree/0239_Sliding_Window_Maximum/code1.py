from sortedcontainers import SortedList

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        
        ans = []
        bst = SortedList(nums[:k - 1])
        for i in range(k - 1, n):
            bst.add(nums[i])
            ans.append(bst[-1])
            bst.remove(nums[i - k + 1])
            
        return ans