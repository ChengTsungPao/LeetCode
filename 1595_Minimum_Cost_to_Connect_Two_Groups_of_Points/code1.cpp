class Solution {
public:
    int memo[12 + 1][4096 + 1];
    int connectTwoGroups(vector<vector<int>>& cost) {
        memset(memo, -1, sizeof(memo));
        return recur(0, 0, cost);
    }
    
    int recur(int group1Idx, int group2, vector<vector<int>>& cost){
        int m = cost.size();
        int n = cost[0].size();
        
        if(group1Idx >= m && group2 >= ((1 << n) - 1)){
            return 0;
        }
        
        if(memo[group1Idx][group2] != -1){
            return memo[group1Idx][group2];
        }
        
        int ans = INT_MAX;
        if(group1Idx < m){
            for(int group2Idx = 0; group2Idx < n; group2Idx++){
                ans = min(ans, cost[group1Idx][group2Idx] + recur(group1Idx + 1, group2 | (1 << group2Idx), cost));
            }
        } else {
            ans = 0;
            for(int group2Idx = 0; group2Idx < n; group2Idx++){
                if((group2 & (1 << group2Idx)) == 0){
                    ans += findGroup1Min(group2Idx, cost);
                }
            }
        }
        return memo[group1Idx][group2] = ans;
    }
    
    int findGroup1Min(int group2Idx, vector<vector<int>>& cost){
        int _min = INT_MAX;
        for(int group1Idx = 0; group1Idx < cost.size(); group1Idx++){
            _min = min(_min, cost[group1Idx][group2Idx]);
        }
        return _min;
    }
};