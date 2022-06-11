from sortedcontainers import SortedList

class MapSum:

    def __init__(self):
        self.bst = SortedList()
        self.score = {}

    def insert(self, key: str, val: int) -> None:
        if key not in self.bst:
            self.bst.add(key)
        self.score[key] = val

    def sum(self, prefix: str) -> int:
        left = self.bst.bisect_left(prefix)
        score, length = 0, len(prefix)
        for i in range(left, len(self.bst)):
            if self.bst[i][:length] == prefix:
                score += self.score[self.bst[i]]
            else:
                break
        return score


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)