class Solution:
    def originalDigits(self, s: str) -> str:
        
        table = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord("a")] += 1
        
        memo = set()
        def recur(index, count):
            
            key = str(index) + "_" + str(count)
            
            if key not in memo:
            
                if sum(count) == 0:
                    return True, ""
                elif index >= 10:
                    return False, ""

                maxTimes = min([count[ord(ch) - ord("a")] // times for ch, times in collections.Counter(table[index]).items()])  
                
                for times in range(maxTimes, -1, -1):
                    
                    for ch in table[index]:
                        count[ord(ch) - ord("a")] -= times

                    isValid, number = recur(index + 1, count)
                    if isValid:
                        return True, str(index) * times + number

                    for ch in table[index]:
                        count[ord(ch) - ord("a")] += times
                        
                memo.add(key)
                    
            return False, ""

        return recur(0, count)[1]