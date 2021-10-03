class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
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
        
        def recur(index, memo = {}):
            
            if index >= len(digits):
                return [""]
            
            ans= []
            rets = recur(index + 1)
            
            for char in table[digits[index]]:
                for ret in rets:
                    ans.append(char + ret)
                    
            return ans
        
        if digits == "":
            return []
        
        return recur(0)
