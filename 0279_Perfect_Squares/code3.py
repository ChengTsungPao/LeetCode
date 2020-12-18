class Solution:
    def numSquares(self, n: int) -> int:
        dp = set([n])
        que = collections.deque()
        que.appendleft((n, 1, float("inf")))
        while que:
            data = que.pop()
            for i in range(min(int(data[0] ** 0.5), data[2]), 0, -1):
                if data[0] - i ** 2 == 0:
                    return data[1]
                if data[0] - i ** 2 not in dp:
                    que.appendleft((data[0] - i ** 2, data[1] + 1, i))
                    dp.add(data[0] - i ** 2)