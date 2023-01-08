class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        personVisited = collections.defaultdict(list)
        for _, person, web in sorted(zip(timestamp, username, website)):
            personVisited[person].append(web)

        def recur(i, vistedTuple, websites):
            if len(vistedTuple) == 3:
                return {vistedTuple}
            elif i == len(websites):
                return set()
            return recur(i + 1, vistedTuple + (websites[i],), websites) | recur(i + 1, vistedTuple, websites)
            
        count = collections.Counter()
        for person, websites in personVisited.items():
            for vistedTuple in recur(0, (), websites):
                count[vistedTuple] += 1

        return list(min([(-times, vistedTuple) for vistedTuple, times in count.items()])[1])