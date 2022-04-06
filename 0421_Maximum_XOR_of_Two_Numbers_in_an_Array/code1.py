class Node:
    def __init__(self):
        self.next = {}
        self.isWord = True
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def changeBit(self, bit):
        if bit == "0":
            return "1"
        else:
            return "0"
        
    def add(self, word):
        node = self.root
        for ch in word:
            if ch not in node.next:
                node.next[ch] = Node()
            node = node.next[ch]
        node.isWord = True
        
    def maxXOR(self, word):
        node = self.root
        ans = ""
        for ch in word:
            nextCh = self.changeBit(ch)
            if nextCh in node.next:
                ans += "1"
            else:
                nextCh = self.changeBit(nextCh)
                ans += "0"
            node = node.next[nextCh]
        return int(ans, 2)

    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        ans = 0
        trie = Trie()
        for num in nums:
            binaryNum = bin(num)[2:].zfill(32)
            trie.add(binaryNum)
            ans = max(ans, trie.maxXOR(binaryNum))
            
        return ans