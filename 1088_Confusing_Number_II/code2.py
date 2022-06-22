class Solution:
    def confusingNumberII(self, n: int) -> int:     
        
        rotateMap = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }

        
        def getAllNumber(index, k, canBigger = False):
            if index == k:
                return 1
            
            ans = 0
            for digit in ["0", "1", "6", "8", "9"]:
                if not canBigger and int(digit) > int(n[index]):
                    continue
                
                ans += getAllNumber(index + 1, k, canBigger or int(digit) < int(n[index]))
                    
            return ans
        
        
        def getNotConfusingNumber(index, k, num = "", canBigger = False):
            if index == k:
                reversedNum = num[:-1][::-1] if len(n) % 2 == 1 else num[::-1]
                num += "".join([rotateMap[d] for d in reversedNum])
                return int(num) <= int(n)
            
            ans = 0
            for digit in ["0", "1", "6", "8", "9"]:
                if not canBigger and int(digit) > int(n[index]):
                    continue
                if index == 0 and int(digit) == 0:
                    continue
                if len(n) % 2 == 1 and index == k - 1 and digit in ["6", "9"]:
                    continue

                ans += getNotConfusingNumber(index + 1, k, num + digit, canBigger or int(digit) < int(n[index]))
                    
            return ans
        
        
        table = [0, 0, 0, 0, 0, 0, 1, 1, 1, 2]
        if n < 10: return table[n]

        n = str(n)
        k = len(n)
        
        countAllNumber = getAllNumber(0, k)
        
        countNotConfusingNumber = 3
        countNotConfusingNumber += getNotConfusingNumber(0, math.ceil(k / 2))
        countNotConfusingNumber += sum([3 * 4 * 5 ** (i // 2 - 1) if i % 2 == 1 else 4 * 5 ** (i // 2 - 1) for i in range(2, k)])
    
        return countAllNumber - countNotConfusingNumber