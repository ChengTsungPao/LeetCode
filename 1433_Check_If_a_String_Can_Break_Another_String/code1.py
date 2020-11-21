class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1.encode()))
        s2 = sorted(list(s2.encode()))
        #print(s1, s2)
        flag = True
        for i in range(len(s1)):
            tmps1 = s1[i] + (s1[i] < 97) * 32
            tmps2 = s2[i] + (s2[i] < 97) * 32
            if tmps1 > tmps2:
                flag = False
                break
        if flag:
            return True
        for i in range(len(s1)):
            tmps1 = s1[i] + (s1[i] < 97) * 32
            tmps2 = s2[i] + (s2[i] < 97) * 32
            if tmps1 < tmps2:
                return False
        return True