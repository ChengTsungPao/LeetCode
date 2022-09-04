# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        
        n = len(s)
        
        stack = []
        bracketsIndex = {}
        
        previ = -1
        numberIndex = {} if not s[-1].isdigit() else {0: n - 1}
        
        commaIndex = n
        nextCommaIndex = {}
        
        for i, ch in enumerate(s):
            if ch == "[":
                stack.append(i)
            elif ch == "]":
                bracketsIndex[stack.pop()] = i
                
            if previ < 0 and (ch.isdigit() or ch == "-"):
                previ = i
            elif previ >= 0 and not ch.isdigit():
                numberIndex[previ] = i - 1
                previ = -1
            
            nextCommaIndex[n + (~i)] = commaIndex
            if s[~i] == ",":
                commaIndex = n + (~i)
            
        def recur(i, j):
            
            NI = NestedInteger()
            
            if s[i] != "[":
                k = numberIndex[i]
                NI.setInteger(int(s[i: k + 1]))
                return NI
                
            k = i + 1
            while k < j:
                if s[k] == "[":
                    NI.add(recur(k, bracketsIndex[k]))
                    k = bracketsIndex[k] + 1
                else:
                    NI.add(recur(k, nextCommaIndex[k] - 1))
                    k = nextCommaIndex[k]
                k += 1
                
            return NI
        
        return recur(0, n - 1)