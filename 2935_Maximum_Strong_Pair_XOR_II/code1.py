class Trie:
    def __init__(self):
        self.root = {"num": -1, "count": 0}
        
    def insert(self, num):
        binary = bin(num)[2:].zfill(20)
        node = self.root
        for d in binary:
            node["count"] += 1
            if d not in node:
                node[d] = {"num": -1, "count": 0}
            node = node[d]
        node["count"] += 1
        node["num"] = num
        
    def remove(self, num):
        binary = bin(num)[2:].zfill(20)
        node = self.root
        for d in binary:
            node["count"] -= 1
            if node[d]["count"] == 1:
                del node[d]
                break
            node = node[d]

    def search(self, num):
        binary = bin(num)[2:].zfill(20)
        
        def _search(node, depth):            
            if node["num"] > 0:
                return num ^ node["num"]
            
            do = binary[depth]
            dr = str(int(not int(binary[depth])))
            
            if dr in node:
                return _search(node[dr], depth + 1)
            elif do in node:
                return _search(node[do], depth + 1)
            else:
                return -float("inf")

        return _search(self.root, 0)
                
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        
        nums = sorted(set(nums))
        n = len(nums)
        
        trie = Trie()

        ans = i = j = 0
        for num in nums:
            down, up = math.ceil(num / 2), num * 2
            
            while i < n and nums[i] < down: 
                trie.remove(nums[i])
                i += 1
                
            while j < n and nums[j] <= up:
                trie.insert(nums[j])
                j += 1

            ans = max(ans, trie.search(num))

        return ans