# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = self.flatten(nestedList)
        self.index = 0
    
    
    def flatten(self, nestedList):
        arr = []
        for nestedListElement in nestedList:
            if nestedListElement.isInteger():
                arr.append(nestedListElement.getInteger())
            else:
                arr += self.flatten(nestedListElement.getList())   
        return arr

    
    def next(self) -> int:
        self.index += 1
        return self.arr[self.index - 1]
        
    
    def hasNext(self) -> bool:
        return self.index < len(self.arr)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())