class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ans = ""
        index = 0
        k = len(num) - k
        while k > 0:
            min_ = "9"
            for i in range(index, len(num) - k + 1):
                if int(num[i]) < int(min_):
                    index = i + 1
                    min_ = num[i]
            ans += min_
            k -= 1
        if ans != "":
            return str(int(ans))
        else:
            return "0"