class Solution:
    
    def findParent(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.findParent(self.parent[x])
        return self.parent[x]
    
    def Union(self, x, y):
        px = self.findParent(x)
        py = self.findParent(y)
        
        if px == py:
            return
        
        if self.size[px] > self.size[py]:
            self.size[px] += self.size[py]
            self.parent[py] = px
        elif self.size[px] < self.size[py]:
            self.size[py] += self.size[px]
            self.parent[px] = py
        else:
            self.size[py] += self.size[px]
            self.parent[px] = py
    
    def longestConsecutive(self, nums: List[int]) -> int:
        
        self.index = {}
        self.size = []
        self.parent = []
        for i in range(len(nums)):
            self.index[nums[i]] = i
            self.size.append(1)
            self.parent.append(i)
        
        for i in range(len(nums)):
            if nums[i] + 1 in self.index:
                self.Union(self.index[nums[i]], self.index[nums[i] + 1])
            
        return max(self.size, default = 0)
