class Solution:
    def countAndSay(self, n: int) -> str:
        def result(_str):
            ans = _str[-1]
            count = 1
            for i in range(len(_str) - 2, -1, -1):
                if _str[i] == ans[-1]:
                    count += 1
                else:
                    ans += str(count) + _str[i]
                    count = 1
            return (ans + str(count))[::-1]
        
        ans = "1"
        for _ in range(n - 1):
            ans = result(ans)
        return ans