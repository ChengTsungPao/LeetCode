class Solution:
    def findNthDigit(self, n: int) -> int:
        
        number_digit = 1
        numbers = 9
        
        while n - number_digit * numbers >= 0:
            n -= number_digit * numbers
            number_digit += 1
            numbers *= 10
            
        startNum = int("9" * (number_digit - 1)) if number_digit > 1 else 0
        startNum += math.ceil(n / number_digit)
        
        return int(str(startNum)[n % number_digit - 1])
