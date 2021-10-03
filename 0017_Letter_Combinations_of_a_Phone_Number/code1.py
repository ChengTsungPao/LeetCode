class Solution:    
    def letterCombinations(self, digits: str) -> List[str]:
        
        # 方法: 利用進位制的概念
        # 範例: digits = "89" => "tw" = "00"、"tx" = "01" ... "vz" = "23"

        table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        ans = []
        maxNum = digits != ""
        
        for digit in digits:
            maxNum *= len(table[digit])
            
        for num in range(maxNum):
            s = ""
            for digit in reversed(digits):
                
                divisor = len(table[digit])
                quotient, remainder = num // divisor, num % divisor
                
                s = table[digit][remainder] + s
                num = quotient
                
            ans.append(s)
            
        return ans
