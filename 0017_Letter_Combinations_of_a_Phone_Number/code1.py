class Solution:    
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits==""):
            ans = []
        else:
            data = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
            def transform(num,long):
                ans = []
                index = len(digits)-1
                while num!=0:
                    tmp = len(data[digits[index]])
                    ans.append(num%tmp)
                    num = num//tmp
                    index -= 1
                for i in range(long-len(ans)):
                    ans.append(0)
                return ans
            ans = []
            length = 1
            for i in digits:
                length *= len(data[i])
            for i in range(length):
                t = transform(i,length)
                s = ""
                for j in range(len(digits)):
                    s += data[digits[j]][t[len(digits)-j-1]]
                ans.append(s)
        return ans