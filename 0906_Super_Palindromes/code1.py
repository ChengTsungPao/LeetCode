class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        
        maxLength = len(right)
        left, right = int(left), int(right)
        
        def isPalindrome(number):
            number = str(number)
            return number == number[::-1]
        
        def recur(number):
            squareNum = 0 if number == "" else pow(int(number), 2)
            if len(number) > maxLength // 2 + 1 or squareNum > right:
                return 0
            return (left <= squareNum and isPalindrome(squareNum)) + sum([recur(str(d) + number + str(d)) for d in range(9 + 1)])
        
        return recur("") + sum([recur(str(d)) for d in range(9 + 1)])