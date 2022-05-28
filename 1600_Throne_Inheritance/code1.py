class Node:
    def __init__(self, name):
        self.name = name
        self.live = True
        self.children = []

        
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Node(kingName)

    def birth(self, parentName: str, childName: str) -> None:
        
        def _birth(node):
            if not node:
                return False
            
            if node.name == parentName and node.live:
                node.children.append(Node(childName))
                return True
            
            for nextNode in node.children:
                if _birth(nextNode):
                    return True
                
            return False

        _birth(self.root)
        
    def death(self, name: str) -> None:
        
        def _death(node):
            if not node:
                return False
            
            if node.name == name:
                node.live = False
                return True
            
            for nextNode in node.children:
                if _death(nextNode):
                    return True
                
            return False
        
        _death(self.root)

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