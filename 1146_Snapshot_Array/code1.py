class SnapshotArray:

    def __init__(self, length: int):
        self.history = []
        self.current = collections.defaultdict(int)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.current[index] = val

    def snap(self) -> int:
        self.history.append(self.current.copy())
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.history[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)