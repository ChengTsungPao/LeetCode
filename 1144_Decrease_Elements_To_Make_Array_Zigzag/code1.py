class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        firstBiggerMove = 0
        preNum = nums[0]
        for i in range(1, n):
            num = nums[i]
            if i % 2 == 0 and preNum >= num:
                move = preNum - num + 1
                preNum = num
            elif i % 2 == 1 and preNum <= num:
                move = num - preNum + 1
                preNum = preNum - 1
            else:
                move = 0
                preNum = num
            firstBiggerMove += move
            
        firstSmallerMove = 0
        preNum = nums[0]
        for i in range(1, n):
            num = nums[i]
            if i % 2 == 1 and preNum >= num:
                move = preNum - num + 1
                preNum = num
            elif i % 2 == 0 and preNum <= num:
                move = num - preNum + 1
                preNum = preNum - 1
            else:
                move = 0
                preNum = num
            firstSmallerMove += move
            
        return min(firstBiggerMove, firstSmallerMove)