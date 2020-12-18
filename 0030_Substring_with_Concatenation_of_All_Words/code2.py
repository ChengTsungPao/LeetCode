class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans, length, total_length = [], len(words[0]), len(words[0]) * len(words)
        words = collections.Counter(words)
        
        for i in range(len(s) - total_length + 1):
            find = collections.defaultdict(int)
            for j in range(i, i + total_length, length):
                if s[j : j + length] in words:
                    find[s[j : j + length]] += 1
                else:
                    break
            if find == words:
                ans.append(i)
                
        return ans
