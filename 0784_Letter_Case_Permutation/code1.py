class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        count = 0
        for i in range(len(S)):
            if(S[i].isalpha()):
                count += 1
        ans = []
        for i in range(2**count):
            s = ""
            k = 0
            tmp = bin(i)[2:].zfill(count)
            for j in range(len(S)):
                if(S[j].isalpha()):
                    if(tmp[k]=="1"):
                        s += S[j].swapcase()
                    else:
                        s += S[j]
                    k += 1
                else:
                    s += S[j]
            ans.append(s)
        return ans