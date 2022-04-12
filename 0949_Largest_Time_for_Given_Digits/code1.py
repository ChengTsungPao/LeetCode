class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
                
        memo = {}
        def permutation(count):
            key = str(count)
            
            if key not in memo:
                if sum(count) == 0:
                    return [[]]
                
                ans = []
                for digit in range(9, -1, -1):
                    if count[digit] == 0:
                        continue
                        
                    count[digit] -= 1
                    for ret in permutation(count):
                        ans.append([digit] + ret)
                    count[digit] += 1
                    
                memo[key] = ans
                
            return memo[key]
        
        def isValid(hour, minute):
            return 0 <= hour <= 23 and 0 <= minute <= 59
        
        count = [0] * 10
        for digit in arr:
            count[digit] += 1
            
        for arr in permutation(count):
            hour, minute = 10 * arr[0] + arr[1], 10 * arr[2] + arr[3]
            if isValid(hour, minute):
                return str(hour).zfill(2) + ":" + str(minute).zfill(2)
            
        return ""