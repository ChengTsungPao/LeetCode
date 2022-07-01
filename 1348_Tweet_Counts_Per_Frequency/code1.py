from sortedcontainers import SortedList

class TweetCounts:

    def __init__(self):
        self.record = collections.defaultdict(SortedList)
        self.timeTable = {
            "minute" : 60,
            "hour"   : 3600,
            "day"    : 86400
        }
        
    def recordTweet(self, tweetName: str, time: int) -> None:
        self.record[tweetName].add(time)
        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        countPerFrequency = []
        timeDelta = self.timeTable[freq]
        timeRecord = self.record[tweetName]
        while startTime < endTime + 1:
            indexRange = timeRecord.bisect_left(startTime), timeRecord.bisect_right(min(startTime + timeDelta - 1, endTime))
            countPerFrequency.append(indexRange[1] - indexRange[0])
            startTime += timeDelta
        return countPerFrequency


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)