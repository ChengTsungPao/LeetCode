class Solution:
    def confusingNumberII(self, n: int) -> int:
        
        rotateMap = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        }
        
        
        def rotated(num):            
            num = str(num)
            
            rotatedNum = ""
            for digit in num[::-1]:
                if digit not in rotateMap:
                    return -1
                rotatedNum += rotateMap[digit]
                
            return int(rotatedNum)
        
        
        def recur(index, canBigger):
            if index == k:
                return [""]
            
            ans = []
            for digit in rotateMap.keys():
                if not canBigger and int(digit) > int(n[index]):
                    continue
                
                for ret in recur(index + 1, canBigger or int(digit) < int(n[index])):
                    ans.append(digit + ret)
                    
            return ans
        
        
        n = str(n)
        k = len(n)
        
        ans = 0
        for num in recur(0, False): 
            num = int(num)
            rotatedNum = rotated(num)
            if rotatedNum > 0 and rotatedNum != num:
                ans += 1
                
        return ans