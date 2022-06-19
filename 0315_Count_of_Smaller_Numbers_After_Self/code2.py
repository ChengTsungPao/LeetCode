class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        
        # time complexity: O(nlogn)
        # space complexity: O(n)
        
        n = len(nums)
        bst = SortedList()
        
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            index = bst.bisect_left(nums[i]) # O(logn)
            ans[i] = index                   # O(1)
            bst.add(nums[i])                 # O(logn)
            
        return ans