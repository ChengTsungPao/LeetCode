class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if(digits==[]): return [1]
        for i in range(len(digits)-1,-1,-1):
            tmp = digits[i] + 1
            if(tmp==10):
                digits[i] = 0
            else:
                digits[i] = tmp
                break
        if(tmp==10):
            digits = [1] + digits
        return digits