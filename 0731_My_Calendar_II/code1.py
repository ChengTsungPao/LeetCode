class MyCalendarTwo:

    def __init__(self):
        self.times = []

        
    def book(self, start: int, end: int) -> bool:

        times = self.times.copy()
        times.insert(bisect.bisect_left(times, (start, 1)), (start, 1))
        times.insert(bisect.bisect_left(times, (end, -1)), (end, -1))

        countMapping = 0
        for time, target in times:
            countMapping += target
            
            if countMapping >= 3:
                return False
            
        self.times = times
            
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)