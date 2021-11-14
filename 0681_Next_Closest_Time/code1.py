class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        nums = set()
        for digit in time:
            if digit != ":":
                nums.add(digit)
        nums = list(nums)
        
        
        dayTime = 24 * 60
        hour, minute = time.split(":")
        startTime = int(hour) * 60 + int(minute)
        
        ans = (dayTime, time)
        for num1 in nums:
            for num2 in nums:
                for num3 in nums:
                    for num4 in nums:
                        hour, minute = num1 + num2, num3 + num4
                        nextTime = hour + ":" + minute
                        if int(hour) < 24 and int(minute) < 60 and nextTime != time:
                            endTime = int(hour) * 60 + int(minute)
                            ans = min(ans, ((endTime - startTime) % dayTime, nextTime))
                        
        return ans[1]
        