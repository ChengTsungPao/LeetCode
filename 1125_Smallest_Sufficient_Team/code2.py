class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        # 將people轉成bit的形式，0代表沒該技能，1代表有該技能
        
        req_skills_index = {}
        for i in range(len(req_skills)):
            req_skills_index[req_skills[i]] = i
            
        people_bit, req_skills_bit = [], 2 ** len(req_skills) - 1
        for i in range(len(people)):
            people_bit.append(0)
            for j in range(len(people[i])):
                people_bit[i] += 2 ** req_skills_index[people[i][j]]

                
        # 利用dp選出目前該技能組合所需之最少員工
        
        dp = {0: []}
        for i in range(len(people_bit)):
            for skills in list(dp.keys()):
                new_skills =  skills | people_bit[i]
                if new_skills not in dp or len(dp[new_skills]) > len(dp[skills]) + 1:
                    dp[new_skills] = dp[skills] + [i]

        return dp[req_skills_bit]
