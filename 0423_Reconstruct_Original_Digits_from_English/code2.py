class Solution:
    def originalDigits(self, s: str) -> str:
        
        table =  ["zero", "two", "six", "eight", "three", "four", "five", "seven", "nine", "one"]
        unique = [   "z",   "w",   "x",     "g",     "t",    "r",    "f",     "v",    "i",   "o"]
        real =   [   "0",   "2",   "6",     "8",     "3",    "4",    "5",     "7",    "9",   "1"]
        
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1
            
        digitTimes = []
        for index in range(10):
            ch = unique[index]
            times = count[ord(ch) - ord("a")]
            digitTimes.append(times)
            
            for ch in table[index]:
                count[ord(ch) - ord("a")] -= times   

        return "".join([digit * times for digit, times in sorted(zip(real, digitTimes))])