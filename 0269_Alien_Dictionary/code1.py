class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        def findFirstDiffCh(word1, word2):
            m = len(word1)
            n = len(word2)
            i = j = 0
            while i < m and j < n:
                if word1[i] != word2[j]:
                    return word1[i], word2[j]
                i += 1
                j += 1
            return "", ""
        
        n = len(words)
        
        allNodes = set()
        graph = collections.defaultdict(set)
        parent = collections.defaultdict(set)
        for i in range(n):
            allNodes |= set(words[i])
            for j in range(i + 1, n):                
                ch1, ch2 = findFirstDiffCh(words[i], words[j])
                if len(ch1) > 0:
                    graph[ch1].add(ch2)
                    parent[ch2].add(ch1)
                elif len(words[i]) > len(words[j]):
                    return ""

        que = collections.deque()
        for ch in allNodes:
            parent[ch] = len(parent[ch])
            if parent[ch] == 0:
                que.appendleft(ch)

        ans = ""
        while que:
            newQue = collections.deque()
            for ch in sorted(que):
                ans += ch
                for nextCh in graph[ch]:
                    parent[nextCh] -= 1
                    if parent[nextCh] == 0:
                        newQue.appendleft(nextCh)
            que = newQue
             
        return ans if len(ans) == len(allNodes) else ""