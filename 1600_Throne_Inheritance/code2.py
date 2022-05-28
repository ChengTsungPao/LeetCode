class Node:
    def __init__(self, name):
        self.name = name
        self.live = True
        self.children = []

        
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)
        self.nodeDict = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        node = self.nodeDict[parentName]
        newNode = Node(childName)
        node.children.append(newNode)
        self.nodeDict[childName] = newNode

    def death(self, name: str) -> None:
        node = self.nodeDict[name]
        node.live = False
        del self.nodeDict[name]

    def getInheritanceOrder(self) -> List[str]:
        
        def getOrder(node):
            if not node:
                return []
            
            ans = [node.name] if node.live else []
            for nextNode in node.children:
                ans.extend(getOrder(nextNode))
                
            return ans
        
        return getOrder(self.root)
       
        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()