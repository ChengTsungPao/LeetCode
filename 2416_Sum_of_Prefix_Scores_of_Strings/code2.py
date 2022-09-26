class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = {}
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
                node["#"] = node.get("#", 0) + 1
        
        ans = [0] * len(words)
        for i, word in enumerate(words):
            node = trie
            for ch in word:
                if ch not in node:
                    break
                node = node[ch]
                ans[i] += node["#"]
                
        return ans