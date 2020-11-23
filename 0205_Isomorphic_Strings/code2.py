class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count, s_status, t_status = 0, {}, {}
        for i in range(len(s)):
            if s[i] in s_status and t[i] in t_status and s_status[s[i]] == t_status[t[i]]:
                continue
            elif s[i] not in s_status and t[i] not in t_status:
                s_status[s[i]] = count
                t_status[t[i]] = count
                count += 1
            else:
                return False
        return True  