class disjoint_set:
    def __init__(self):
        self.parent = {}
        self.weight = {}
        self.name = {}
        
    def build(self, name, email):
        if email not in self.parent:
            self.parent[email] = email
            self.weight[email] = 1
            self.name[email] = name
            
    def findParent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def union(self, node1, node2):
        p1 = self.findParent(node1)
        p2 = self.findParent(node2)
        
        if p1 == p2:
            return
        
        if self.weight[p1] < self.weight[p2]:
            self.parent[p1] = p2
        elif self.weight[p1] > self.weight[p2]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.weight[p2] += 1
            

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        DS = disjoint_set()
        
        emails = set()
        for account in accounts:
            name, email = account[0], account[1]
            emails.add(email)
            
            DS.build(name, email)
            for e in account[2:]:
                DS.build(name, e)
                DS.union(email, e)
                emails.add(e)

        mergeAccounts = collections.defaultdict(list) 
        for email in emails:
            mergeAccounts[DS.findParent(email)].append(email)

        ans = []
        for email in mergeAccounts.keys():
            ans.append([DS.name[email]] + sorted(mergeAccounts[email]))
            
        return ans