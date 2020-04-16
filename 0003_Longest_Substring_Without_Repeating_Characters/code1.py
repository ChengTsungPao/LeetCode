class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s)==0): return 0
        tmp = set(s[0])
        ans = 1
        for i in range(len(s)-1):
            if(tmp&set(s[i+1])==set()):
                tmp.add(s[i+1])
            else:
                if(len(tmp) > ans): ans = len(tmp)
                tmp = set(s[(i-(s[i:0:-1]+s[0]).index(s[i+1]))+1:i+1+1])
        if(len(tmp) > ans): ans = len(tmp)
        return ans