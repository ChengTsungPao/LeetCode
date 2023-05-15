class FrequencyTracker:

    def __init__(self):
        self.countNum = collections.defaultdict(int)
        self.collectFreq = collections.defaultdict(set)

    def add(self, number: int) -> None:
        freq = self.countNum[number]
        if freq > 0:
            self.collectFreq[freq].remove(number)
            if len(self.collectFreq[freq]) == 0: del self.collectFreq[freq]
        self.countNum[number] += 1
        self.collectFreq[freq + 1].add(number)
        
    def deleteOne(self, number: int) -> None:
        if number in self.countNum:
            freq = self.countNum[number]
            self.collectFreq[freq].remove(number)
            if len(self.collectFreq[freq]) == 0: del self.collectFreq[freq]
            self.countNum[number] -= 1
            if freq - 1 > 0: self.collectFreq[freq - 1].add(number)
            if freq - 1 == 0: del self.countNum[number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.collectFreq

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)