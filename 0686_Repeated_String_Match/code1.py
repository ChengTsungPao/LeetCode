class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        # a = "abcd", b = "cdabcdabcda" ==> s = "abcdabcd" => s = "bcd" + "abcdabcd"
        
        if len(b) % len(a) == 0:
            ans = len(b) // len(a) - 1
        else:
            ans = len(b) // len(a)
        
        s = a * ans
        remainderLen = len(b) - len(s)
        if s + a[:remainderLen] == b or a[-remainderLen:] + s == b:
            return ans + 1
        
        s = a[-remainderLen:] + s
        for i in range(len(a)):
            s = s[1:] + a[i]
            if s == b:
                # remainderLen
                if i < remainderLen:
                    return ans + 2
                else:
                    return ans + 1
            
        return -1
