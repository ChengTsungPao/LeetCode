from sortedcontainers import SortedList

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leads = []
        
        bst = SortedList()
        count = collections.defaultdict(int)
        personTime = collections.defaultdict(int)
        
        for person, time in zip(persons, times):
            if person in personTime:
                bst.remove((count[person], personTime[person], person))
                
            count[person] += 1
            personTime[person] = time
            
            bst.add((count[person], personTime[person], person))
            self.leads.append(bst[-1][-1])

    def q(self, t: int) -> int:
        index = bisect.bisect_right(self.times, t) - 1
        return self.leads[index] if index < len(self.leads) else self.leads[-1]
        

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)