class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        symbol = numerator ^ denominator < 0 and numerator != 0
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part, decimal_part = str(numerator // denominator), ""
        numerator %= denominator
        if numerator == 0:
            return "-" * symbol + integer_part
        number, index, flag = {}, 0, False
        while len(integer_part) + len(decimal_part) + 1 < 10 ** 4:
            numerator *= 10
            quotient, remainder = numerator // denominator, numerator % denominator
            if remainder == 0:
                decimal_part += str(quotient)
                break
            elif (quotient, numerator) not in number:
                number[quotient, numerator] = index
                decimal_part += str(quotient)
                numerator = remainder
                index += 1
            else:
                flag = True
                break
        if flag: 
            return "-" * symbol + integer_part + "." + decimal_part[:number[quotient, numerator]] + "(" + decimal_part[number[quotient, numerator]:] + ")"
        else:
            return "-" * symbol + integer_part + "." + decimal_part