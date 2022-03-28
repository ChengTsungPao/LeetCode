class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        
        ans = 0
        i = 0
        j = len(people) - 1
        
        while i <= j:
            if i <= j - 1 and people[j - 1] + people[j] <= limit:
                j -= 2
            elif people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1

            ans += 1
        
        return ans