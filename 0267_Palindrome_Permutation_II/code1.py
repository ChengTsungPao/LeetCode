class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        count = collections.Counter(s)
        
        midChar = ""
        hasOdd = False
        for ch in count.keys():            
            if count[ch] % 2 == 1:
                if hasOdd:
                    return []
                hasOdd = True
                midChar = ch
                count[midChar] -= 1
        
        memo = {}
        def recur(count):
            key = count.values()
            if sum(key) == 0:
                return [midChar]
            
            if str(key) not in memo:
                ret = []
                for ch in count.keys():
                    if count[ch] == 0:
                        continue

                    count[ch] -= 2
                    for i in recur(count):
                        ret.append(ch + i + ch)
                    count[ch] += 2
                    
                memo[str(key)] = ret
                    
            return memo[str(key)]
        
        return recur(count)