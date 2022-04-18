class Leaderboard:
    def __init__(self):
        self.container = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.container[playerId] += score
        
    def top(self, K: int) -> int:
        scores = 0
        for score in sorted(self.container.values(), reverse = True):
            scores += score
            K -= 1
            if K == 0:
                break
        return scores
        
    def reset(self, playerId: int) -> None:
        del self.container[playerId]

        
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)