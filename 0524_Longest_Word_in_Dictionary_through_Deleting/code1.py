class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        ans = []
        for i in range(len(d)):
            ans += "",
        for i in range(len(s)):
            for j in range(len(d)):                
                if d[j]!="":
                    if s[i]==d[j][0]:
                        ans[j] += d[j][0]
                        d[j] = d[j][1:len(d[j])]
        for i in range(len(d)):
            if d[i]!="":
                ans[i]=""
                
        max = 0
        answer = ""
        for i in range(len(ans)):
            if len(ans[i])>max:
                max = len(ans[i])
                answer = ans[i]
            elif len(ans[i])==max:
                for j in range(len(answer)):
                    if ord(answer[j])>ord(ans[i][j]):
                        max = len(ans[i])
                        answer=ans[i]
                        break 
                    elif ord(answer[j])<ord(ans[i][j]):
                        break
        return answer