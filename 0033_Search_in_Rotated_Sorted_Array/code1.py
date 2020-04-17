class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if(nums == []): return -1
            
        left = 0
        right = len(nums) - 1        
        while left < right:
            if(nums[(left + right) // 2] == nums[left]):
                left = right
            elif(nums[(left + right) // 2] > nums[left]):
                left = (left + right) // 2
            else:
                right = (left + right) // 2
        if(right != len(nums)-1 or (right == len(nums)-1 and nums[right] < nums[0])):
            nums[:len(nums)-right], nums[len(nums)-right:] = nums[right:], nums[:right]
        else:
            right = 0
        
        index = bisect.bisect_left(nums, target)
        if(index == len(nums) or nums[index] != target):
            return -1
        else:
            if(index - (len(nums) - right) >= 0):
                return index - (len(nums) - right)
            else:
                return index + right
