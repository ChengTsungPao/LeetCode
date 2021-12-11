class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        
        findParent = collections.defaultdict(set)
        findChild= collections.defaultdict(set)
        noParent = set(org)
        allMember = set()
        
        for seq in seqs:
            allMember.add(seq[-1])
            for i in range(len(seq) - 1):
                findChild[seq[i]].add(seq[i + 1])
                findParent[seq[i + 1]].add(seq[i])
                noParent -= set([seq[i + 1]])
                allMember.add(seq[i])
                                  

        if allMember != set(org):
            return False
      
        index = 0        
        while noParent:

            if len(noParent) > 1:
                return False
            
            n = noParent.pop()
            allMember.remove(n)

            if org[index] != n:
                return False
            else:
                index += 1
            
            for child in findChild[n]:
                findParent[child] -= set([n])
                
                if len(findParent[child]) == 0:
                    noParent.add(child)
                    del findParent[child]
                    
            del findChild[n]
  
        return len(allMember) == 0