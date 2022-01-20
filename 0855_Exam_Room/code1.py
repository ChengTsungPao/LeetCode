class ExamRoom:

    def __init__(self, n: int):
        self.seatArray = []
        self.size = n - 1
        
    def seat(self) -> int:
        if len(self.seatArray) == 0:
            self.seatArray.append(0)
            return 0
        else:
            choose = max((abs(0 - self.seatArray[0]), 0), (abs(self.size - self.seatArray[-1]), -self.size))
            for i in range(1, len(self.seatArray)):
                seatPos = (self.seatArray[i] + self.seatArray[i - 1]) // 2
                distance = min(seatPos - self.seatArray[i - 1], self.seatArray[i] - seatPos)
                choose = max(choose, (distance, -seatPos))
            seatPos = -choose[-1]
            self.seatArray.insert(bisect.bisect_left(self.seatArray, seatPos), seatPos)
            return seatPos

    def leave(self, p: int) -> None:
        self.seatArray.remove(p)
        

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)