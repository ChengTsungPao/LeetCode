class Binary_Indexed_Tree():
    def __init__(self, n):
        self.tree = [0] * (n + 1)
        
    def lowbit(self, x):
        return x & -x
    
    def update(self, index, delta):
        while index < len(self.tree):
            self.tree[index] += delta
            index += self.lowbit(index)
            
    def quary(self, index):
        ans = 0
        while index > 0:
            ans += self.tree[index]
            index -= self.lowbit(index)
        return ans


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        # time complexity: O(nlogn)
        # space complexity: O(n)
        
        # 概念: 將Binary_Indexed_Tree的delta都設為1，來統計數量
        # 方法: 由右而左update，在quary的時候只會有該index右邊的數字參與，且只有較小的數字(rank)會被加起來 (因為有sort)
        # 注意: 但須注意不能quary與自己大小相同的數字 (rank[nums[i]] - 1)
        
        # 比起另一個方法多了一個sort，速度會較慢，但較省空間，且能處理有小數點的情況
        
        rank = {}
        sorted_nums = sorted(set(nums))
        for i in range(len(sorted_nums)):
            rank[sorted_nums[i]] = i + 1
        
        BIT = Binary_Indexed_Tree(len(sorted_nums))
        
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            ans.append(BIT.quary(rank[nums[i]] - 1))
            BIT.update(rank[nums[i]], 1)
            
        return ans[::-1]