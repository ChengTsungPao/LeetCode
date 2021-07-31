class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        ans, sorted_array = [], []
        for i in range(len(nums) - 1, -1, -1):
            index = bisect.bisect_left(sorted_array, nums[i])
            ans.append(index)
            sorted_array.insert(index, nums[i])
        ans.reverse()
            
        return ans
