class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        personVisited = collections.defaultdict(list)
        for _, person, web in sorted(zip(timestamp, username, website)):
            personVisited[person].append(web)

        def recur(i, visitedTuple, websites):
            if len(visitedTuple) == 3:
                return {visitedTuple}
            elif i == len(websites):
                return set()
            return recur(i + 1, visitedTuple + (websites[i],), websites) | recur(i + 1, visitedTuple, websites)
            
        count = collections.Counter()
        for person, websites in personVisited.items():
            for visitedTuple in recur(0, (), websites):
                count[visitedTuple] += 1

        return list(min([(-times, visitedTuple) for visitedTuple, times in count.items()])[1])