class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = set()
        que = collections.deque()
        for w in wordDict:
            if(w == s[:len(w)]):
                dp.add(s[len(w):])
                que.insert(0, s[len(w):])
        while que:
            if(que[-1] == ""):
                return True
            for w in wordDict:
                if(que[-1][len(w):] not in dp and w == que[-1][:len(w)]):
                    dp.add(que[-1][len(w):])
                    que.insert(0, que[-1][len(w):])
            que.pop()
        return False