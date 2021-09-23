class TreeNode:
    def __init__(self, kind = -1):
        self.isWord = [False, False] # [word, reverseWord]
        self.index = [-1, -1]
        self.node = {}

class Trie:

    def __init__(self):
        self.tree = TreeNode()

    def insert(self, word, index, kind):
        pointer = self.tree
        for char in word:
            if char not in pointer.node:
                pointer.node[char] = TreeNode()
            pointer = pointer.node[char]
        pointer.isWord[kind] = True
        pointer.index[kind] = index

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
            
        def start_word(root):
            if root == {}:
                return []
            
            ans = []
            if root.isWord[0]:
                for index in end_word(root, 1, ""):
                    if root.index[0] != index:
                        ans.append((root.index[0], index))
            if root.isWord[1]:
                for index in end_word(root, 0, ""):
                    if root.index[1] != index:
                        ans.append((index, root.index[1]))
                        
            for char in root.node.keys():
                ans += start_word(root.node[char])
                
            return ans
            
        
        def end_word(root, kind, str_):
            if root == {}:
                return []
            
            ans = []
            if root.isWord[kind] and str_ == str_[::-1]:
                ans.append(root.index[kind])
            
            for char in root.node.keys():
                ans += end_word(root.node[char], kind, str_ + char)
            
            return ans

        trie = Trie()
        for index in range(len(words)):
            trie.insert(words[index], index, 0)
            trie.insert(words[index][::-1], index, 1)
            
        return set(start_word(trie.tree))