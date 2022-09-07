class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        def isCycle(index, mark):
            startNum = nums[index]
            if type(nums[(index + startNum) % n]) == str or index == (index + startNum) % n:
                nums[index] = mark
                return False
            
            nums[index] = mark
            index = (index + startNum) % n
            while type(nums[index]) == int:
                num = nums[index]
                if startNum ^ nums[index] < 0 or index == (index + num) % n:
                    return False
                nums[index] = mark
                index = (index + num) % n

            return nums[index] == mark
                
        for index in range(n):
            if type(nums[index]) == int and isCycle(index, str(index)):
                return True
            
        return False