class Node:
    def __init__(self, leftIndex, rightIndex, booked = False):
        # booked = True  => 整段區間都已經booked
        # booked = False => 區間中存在沒booked的子區段
        self.left = None
        self.right = None
        self.range = (leftIndex, rightIndex)
        self.booked = booked
    
    
class SegmentTree:
    def __init__(self):
        self.root = Node(0, 10 ** 9 + 1)
    
    def update(self, root, leftIndex, rightIndex):
        # 找到一個子樹他的Range都在要booked的範圍內，將其狀態設定為booked = True 
        # (在這邊可以想像會有很多區段在leftIndex ~ rightIndex之間，且booked = True)
        if leftIndex <= root.range[0] and root.range[1] <= rightIndex:
            root.booked = True
            return
        
        rangeMid = (root.range[0] + root.range[1]) // 2
        
        # 範圍有涵蓋到左邊子樹，代表須建立一個新的左子數
        if leftIndex < rangeMid:
            if not root.left:
                root.left = Node(root.range[0], rangeMid)
            self.update(root.left, leftIndex, rightIndex)
            
        # 範圍有涵蓋到右邊子樹，代表須建立一個新的右子數
        if rightIndex > rangeMid:
            if not root.right:
                root.right = Node(rangeMid, root.range[1])
            self.update(root.right, leftIndex, rightIndex)

    def quary(self, root, leftIndex, rightIndex):
        # 只要找到某一個區段booked = True (也就是區段root.range)，代表leftIndex ~ rightIndex之間有被booked過了
        # (可以想像區段root.range內都被booked了，且因為root.range和leftIndex ~ rightIndex有重疊，所以無法在booked)
        if root.booked:
            return True
        
        rangeMid = (root.range[0] + root.range[1]) // 2
        
        # 範圍有涵蓋到左邊子樹，所以往左子樹走，看看是否有booked
        if leftIndex < rangeMid:
            if root.left and self.quary(root.left, leftIndex, rightIndex):
                return True
            
        # 範圍有涵蓋到右邊子樹，所以往左子樹走，看看是否有booked
        if rangeMid < rightIndex :
            if root.right and self.quary(root.right, leftIndex, rightIndex):
                return True
            
        # 若左右子樹都沒有booked就回傳False
        return False

        
class MyCalendar:
    def __init__(self):
        self.ST = SegmentTree()
        
    def book(self, start: int, end: int) -> bool:
        if self.ST.quary(self.ST.root, start, end) == False:
            self.ST.update(self.ST.root, start, end)
            return True
        else:
            return False
        

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)