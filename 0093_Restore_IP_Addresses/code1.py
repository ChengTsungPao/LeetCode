class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        n = len(s)
        
        if n > 3 * 4:
            return []
        
        def isValid(IP):
            return not (int(IP) > 255 or (len(IP) >= 2 and IP[0] == "0"))
        
        memo = {}
        def recur(index, cut):
            
            if (index, cut) not in memo:
            
                if index >= n:
                    return []
                elif cut == 0:
                    currentIP = s[index:]
                    return [currentIP] if isValid(currentIP) else []

                ans, currentIP = [], ""
                for i in range(index, n):
                    currentIP += s[i]
                    if not isValid(currentIP):
                        break

                    for IP in recur(i + 1, cut - 1):
                        ans.append(currentIP + "." + IP)

                memo[index, cut] = ans
                    
            return memo[index, cut]
        
        return recur(0, 3)