class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.result = self.setup(persons)
        self.times = times
    
    def setup(self, persons):
        result = []
        count = collections.defaultdict(int)
        last_person_index = {}
        
        for index, person in enumerate(persons):
            count[person] += 1
            last_person_index[person] = index
            result.append(max(count.items(), key = lambda element: (element[1], last_person_index[element[0]]))[0])
            
        return result

    def q(self, t: int) -> int:
        index = bisect.bisect_left(self.times, t)
        if index >= len(self.times) or self.times[index] != t:
            index -= 1
            
        return self.result[index]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)