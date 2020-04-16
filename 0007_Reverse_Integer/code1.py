class Solution:
    def reverse(self, x: int) -> int:
        if(x > 0):
            tmp = int(str(x)[::-1])
            if(-2**31 < tmp < (2**31)-1):
                return tmp
            else:
                return 0;
        else:
            tmp = -int(str(-x)[::-1])
            if(-2**31 < tmp < (2**31)-1):
                return tmp
            else:
                return 0;