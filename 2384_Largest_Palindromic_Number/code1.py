class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        count = [0] * 10
        for digit in num:
            digit = int(digit)
            count[digit] += 1
        
        half_largest_num = ""
        for digit in range(9, -1, -1):
            if not (half_largest_num == "" and digit == 0):
                c = count[digit] // 2
                half_largest_num += str(digit) * c
                count[digit] -= c * 2
        
        largest_num = ""
        if half_largest_num == "":
            for digit in range(9, 0, -1):
                if count[digit] > 0:
                    largest_num = str(digit)
                    break
        elif sum(count) == 0:
            largest_num = half_largest_num + half_largest_num[::-1]
        else:
            for digit in range(9, -1, -1):
                if count[digit] > 0:
                    largest_num = half_largest_num + str(digit) + half_largest_num[::-1]
                    break
                    
        return "0" if largest_num == "" else largest_num