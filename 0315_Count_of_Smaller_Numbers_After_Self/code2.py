class Binary_Indexed_Tree:
    
    def __init__(self, size):
        self.size = size + 1
        self.data = [0 for _ in range(self.size)]
        
    def lowbit(self, index):
        return index & (-index)
        
    def update(self, index, delta):
        while index < self.size:
            self.data[index] += delta
            index += self.lowbit(index)
            
    def query(self, index):
        s = 0
        while index > 0:
            s += self.data[index]
            index -= self.lowbit(index)
        return s

class Solution:
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        # step1 => 先做反轉
        # step2 => 計算每個num的排名n
        # step3 => 利用Binary_Indexed_Tree進行操作
        #          update: 將 index = n + 1 的位置更新成 1
        #          query : 計算 index = 1 ~ n + 1 的總和
        #
        # 註: 更新有先後順序，因此不會算到比自己index小的num 
        
        nums.reverse()
        
        tree = Binary_Indexed_Tree(len(nums))
        
        ranks = {}
        for rank, num in enumerate(sorted(set(nums))):
            ranks[num] = rank
        
        ans = []
        for num in nums:
            ans.append(tree.query(ranks[num]))
            tree.update(ranks[num] + 1, 1)
        ans.reverse()
            
        return ans
