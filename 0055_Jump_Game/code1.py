class Solution:
    def canJump(self, nums: List[int]) -> bool:
        flag = True
        index = -1
        for i in range(len(nums) - 2, -1, -1):
            if(nums[i] == 0 and flag):
                index = i
                flag = False
            elif(index - i < nums[i]):
                flag = True
        return flag