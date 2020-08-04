class ListNode:
    def __init__(self, x):
        self.val = x
        self.mark = False
        self.next = []

class WordDictionary(ListNode):

    def __init__(self):                
        self.dic = ListNode(" ")
        """
        Initialize your data structure here.
        """
        
    def addWord(self, word: str) -> None:
        flag = True
        index = 0
        temp = self.dic
        while(flag):
            flag = False
            for n in temp.next:
                if(n.val==word[index]):
                    index += 1
                    flag = True
                    temp = n
                    break
            if(index==len(word)):
                break

        for i in range(index,len(word)):
            tmp = ListNode(word[i])
            temp.next.append(tmp)
            temp = tmp
        temp.mark = True      
        """
        Adds a word into the data structure.
        """
        
    def search(self, word: str) -> bool:
        s = ""
        def dfs(node):
            nonlocal s
            for n in node.next:
                if(len(s) < len(word)):
                    if(n.val!=word[len(s)] and word[len(s)]!="."):
                        continue
                    elif(n.mark==True and len(s)+1==len(word)):
                        return True
                else:
                    return False
                tmp = s
                s += n.val
                _bool = dfs(n)
                if(_bool==True):
                    return True
                s = tmp
            return False
                
        if(dfs(self.dic)):
            return True
        else:
            return False
                
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)