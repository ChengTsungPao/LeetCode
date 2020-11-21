class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        a = num
        if num[0] == "1":
            for i in range(1, len(num)):
                if num[i] != "0" and num[i] != "1":
                    a = a.replace(num[i], "0")
                    break
        else:
            a = a.replace(num[0], "1") 
        b = num
        for i in range(len(num)):
            if num[i] != "9":  
                b = b.replace(num[i], "9")
                break
        return int(b) - int(a)