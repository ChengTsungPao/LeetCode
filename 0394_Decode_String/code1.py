class Solution:
    def decodeString(self, s: str) -> str:
        cut = []
        sum = -1
        for str in s.split("["):
            cut.append(sum)
            sum += len(str)+1
        for i in range(len(cut)-1,0,-1):
            n = cut[i]-1
            while 1==1:
                try:
                    int(s[n])
                    n -= 1
                except:
                    n += 1
                    break
            num = int(s[n:cut[i]])
            j = cut[i]
            while s[j]!="]":
                j += 1            
            expand = s[cut[i]+1:j]*num
            s = s[:n]+expand+s[j+1:]
            
        return s