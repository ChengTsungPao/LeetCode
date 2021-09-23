class trie:
    
    def __init__(self):
        self.tree = {}
    
    def add(self, word, val):
        node = self.tree
        for s in word:
            if s not in node:
                node[s] = {"val": 0}
            node = node[s]
        node["val"] = val
        
    def query(self, word):

        node = self.tree
        for s in word:
            if s not in node:
                return 0
            node = node[s]

        def recur(node):
            if len(node) == 1:
                return node["val"]
            ans = node["val"]
            for key in node.keys():
                if key != "val":
                    ans += recur(node[key])
            return ans
        
        return recur(node)

class MapSum:

    def __init__(self):
        self.trie = trie()        

    def insert(self, key: str, val: int) -> None:
        self.trie.add(key, val)

    def sum(self, prefix: str) -> int:
        return self.trie.query(prefix)
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)