class Solution:
    def numSquares(self, n: int) -> int:
        que = collections.deque()
        que.appendleft((n, 1))
        while que:
            data = que.pop()
            for i in range(int(data[0] ** 0.5), 0, -1):
                if data[0] - i ** 2 == 0:
                    return data[1]
                que.appendleft((data[0] - i ** 2, data[1] + 1))