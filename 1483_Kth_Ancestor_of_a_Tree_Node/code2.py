class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        # 1 <= k <= 5 * 10 ** 4 => log(5 * 10 ** 4) = 15.6
        self.dp = [parent.copy()] + [[0] * n for _ in range(15)]
        for step in range(1, 15 + 1):
            for node in range(n):
                nextNode = self.dp[step - 1][node]
                self.dp[step][node] = self.dp[step - 1][nextNode] if nextNode >= 0 else -1
    
    @functools.lru_cache(None)
    def getKthAncestor(self, node: int, k: int) -> int:
        if k == 0 or node == -1:
            return node
        step = math.floor(math.log(k, 2))
        nextNode = self.dp[step][node]
        return self.getKthAncestor(nextNode, k - pow(2, step))
            

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
