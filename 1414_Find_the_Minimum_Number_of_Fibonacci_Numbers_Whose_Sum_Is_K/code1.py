class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        data = [1, 1]
        answer = 0
        while 1 == 1:
            next = data[-1] + data[-2]
            if(next > k):
                break
            else:
                data.append(next)
        data.reverse()
        def dfs(ans, k):
            nonlocal data
            nonlocal answer
            if(k < 0):
                return
            elif(k == 0):
                answer = len(ans)
                return True
            for n in data:
                if(dfs(ans + [n], k - n)):
                    return True
        dfs([], k)
        return answer