class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        
        indices = collections.defaultdict(list)
        for index, rating in enumerate(ratings):
            indices[rating].append(index)

        ans = [0] * n
        for rating in sorted(indices.keys()):
            for index in indices[rating]:
                candy = 1
                if index - 1 >= 0 and ratings[index - 1] < ratings[index]: 
                    candy = max(candy, ans[index - 1] + 1)
                if index + 1 <  n and ratings[index] > ratings[index + 1]: 
                    candy = max(candy, ans[index + 1] + 1)
                ans[index] = candy

        return sum(ans)