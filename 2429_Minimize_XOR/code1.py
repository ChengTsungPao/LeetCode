class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        # count num2 bit
        count = 0
        while num2 > 0:
            num2 -= num2 & -num2
            count += 1
        
        # remove num1 bit
        x = 0
        while num1 > 0 and count > 0:
            highBit = 1 << int(math.log(num1, 2))
            num1 -= highBit
            x += highBit
            count -= 1
            
        if count == 0:
            return x

        # add reminder bit
        digit = 0
        tempx = x
        while count > 0:
            if tempx & 1 == 0:
                x += 1 << digit
                count -= 1
            tempx >>= 1
            digit += 1
            
        return x
