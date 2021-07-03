class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        def recur(current_bit, people_bit, index, memo = {}):
            
            if (current_bit, index) not in memo:

                if current_bit == req_skills_bit:
                    return [[]]

                memo[current_bit, index] = []
                for i in range(index, len(people_bit)):
                    if current_bit | people_bit[i][0] > current_bit:
                        for j in recur(current_bit | people_bit[i][0], people_bit, i + 1):
                            memo[current_bit, index].append([people_bit[i][1]] + j)

            return memo[current_bit, index]
                
        req_skills_index = {}
        for i in range(len(req_skills)):
            req_skills_index[req_skills[i]] = i
            
        for i in range(len(people)):
            people[i].append(i)
        people.sort(key = len, reverse = True)
            
        people_bit, req_skills_bit = [], 2 ** len(req_skills) - 1
        for i in range(len(people)):
            people_bit.append([0, people[i][-1]])
            for j in range(len(people[i]) - 1):
                people_bit[i][0] += 2 ** req_skills_index[people[i][j]]
        
        return min(recur(0, people_bit, 0) , key = len)