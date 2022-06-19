class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        # time complexity: O(n^2)
        # space complexity: O(n)
        
        n = len(nums)
        
        ans = [0] * n
        sorted_array = []
        for i in range(n - 1, -1, -1):
            index = bisect.bisect_left(sorted_array, nums[i])  # O(logn)
            ans[i] = index                                     # O(1)
            sorted_array.insert(index, nums[i])                # O(n)
            
        return ans